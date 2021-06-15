set nu
set ignorecase
set smartcase
set scrolloff=3
set backspace=indent,eol,start  " more powerful backspacing
set t_Co=256

execute pathogen#infect()

let mapleader="\<space>"
let maplocalleader="-"
let g:python3_host_prog="/nfs/scistore03/vicosgrp/jraices/.cache/pip/wheels/db/12/4a/6d237365156bc58da371a113ae26656dc160fa1ee9c460c4be"

syntax enable
filetype plugin indent on

syntax on

set cursorline

hi CursorLine term=none cterm=none ctermbg=235

colorscheme molokai

:command WQ wq
:command Wq wq
:command W w
:command Q q

inoremap " ""<left>
inoremap ' ''<left>
inoremap ( ()<left>
inoremap [ []<left>
inoremap { {}<left>
inoremap {<CR> {<CR>}<ESC>O
inoremap {;<CR> {<CR>};<ESC>O

