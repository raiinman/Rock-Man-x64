#!/usr/bin/env python3
"""Fail closed if the updater modified anything outside its exact output contract."""
import argparse
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET
from update_tracker import ROOT, OUTPUTS, START, END, Invalid, need

def git(root,*args):
    return subprocess.run(['git',*args],cwd=root,capture_output=True,check=True).stdout

def outside_marker(value):
    need(value.count(START)==1 and value.count(END)==1,'invalid README markers')
    before,rest=value.split(START);_,after=rest.split(END)
    return before,after

def check_content(name, content, previous_readme):
    if name=='README.md':
        need(outside_marker(previous_readme)==outside_marker(content),'README changed outside generated block')
    if name.endswith('.svg'):
        raw=content.replace('http://www.w3.org/2000/svg','').lower()
        need(not any(s in raw for s in ('<!doctype','<!entity','url(','http://','https://','javascript:','data:','@import')), 'external/entity SVG content')
        svg=ET.fromstring(content)
        allowed={'svg':{'width','height','viewBox','role','aria-labelledby'},'title':{'id'},'desc':{'id'},
                 'rect':{'x','y','width','height','rx','fill','stroke'},'text':{'x','y','font-family','font-size','font-weight','fill','letter-spacing'},'path':{'d','fill','stroke','stroke-width'}}
        for e in svg.iter():
            tag=e.tag.split('}')[-1]
            need(tag in allowed,'active SVG element')
            need(set(e.attrib)<=allowed[tag],'unapproved SVG attribute')
            for name,value in e.attrib.items():
                need(not any(s in value.lower() for s in ('url(', '://', 'javascript:', 'data:')), 'external parsed SVG value')
                if name in ('fill','stroke'):
                    need(re.fullmatch(r'#[0-9a-fA-F]{6}|none',value) is not None,'SVG paint must be a literal color')

def check(root,clean=False):
    root=Path(root).resolve()
    raw=git(root,'status','--porcelain=v1','-z','--untracked-files=all')
    records=raw.split(b'\0');paths=[]
    for record in records:
        if not record:continue
        status=record[:2].decode('ascii');name=record[3:].decode('utf-8')
        need('R' not in status and 'C' not in status,'renames/copies are not generated outputs')
        paths.append(name)
    if clean:need(not paths,'working tree not clean before generation')
    need(set(paths)<=set(OUTPUTS),'unauthorized dirty paths: '+', '.join(sorted(set(paths)-set(OUTPUTS))))
    staged=list(filter(None,git(root,'diff','--cached','--name-only','-z').decode().split('\0')))
    need(set(staged)<=set(OUTPUTS),'unauthorized staged paths')
    previous=git(root,'show','HEAD:README.md').decode()
    for name in paths:
        target=root/name
        need(target.is_file() and not target.is_symlink(),'generated outputs must be ordinary files')
        need(target.resolve().is_relative_to(root),'output escaped root')
        check_content(name,target.read_text(),previous)
    for name in staged:
        mode=git(root,'ls-files','--stage','--',name).decode().split()[0]
        need(mode=='100644','generated index entry must be a regular nonexecutable file')
        check_content(name,git(root,'show',':'+name).decode(),previous)
    git(root,'diff','--check')
    return paths

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--clean',action='store_true');a=p.parse_args()
    try:paths=check(a.root,a.clean)
    except (Invalid,OSError,ValueError,subprocess.CalledProcessError) as e:
        print('GENERATED-PATH GUARD REFUSED: '+str(e),file=sys.stderr);return 1
    print('GENERATED-PATH GUARD PASS: '+(', '.join(paths) or 'clean'));return 0

if __name__=='__main__':sys.exit(main())
