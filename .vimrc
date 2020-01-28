" .vimrc

" colorscheme ron

syntax enable
filetype indent on

" set nu sc cul wmnu sm lz
set number			" set nu
set showcmd         " set sc
set cursorline      " set cul
set wildmenu        " set wmnu
set showmatch       " set sm
set lazyredraw      " set lz

" set ts=4 sts=4 sw=4 et sta
set tabstop=4		" set ts=4
set softtabstop=4	" set sts=4
set shiftwidth=4    " set sw=4
set expandtab		" set et
set smarttab        " set sta

" set is hls
set incsearch       " set is
set hlsearch        " set hls

" leader is \ by default
" let mapleader=","
" inoremap jk <esc>
nnoremap <leader><space> :nohlsearch<CR>

set foldenable          " set fen
set foldlevelstart=10   " set fdls=10
set foldnestmax=10      " set fdn=10
nnoremap <space> za
set foldmethod=indent   " set fdm=indent

nnoremap j gj
nnoremap k gk
" nnoremap B ^
" nnoremap E $
" nnoremap gV `[v`]

map <c-h> <c-w>h
map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-l> <c-w>l



" Legacy:
" =======

" map <f4> :!time python %
" map <f5> :!time python %<cr>

" if has("autocmd")
" 	augroup templates
" 		autocmd BufNewFile *.c 0r ~/.vim/templates/skeleton.c
" 	augroup END
" endif
