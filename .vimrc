" .vimrc

" colorscheme ron

syntax enable
filetype indent on

" set nu sc cul wmnu sm lz
set number
set showcmd
set cursorline
set wildmenu
set showmatch
set lazyredraw

" set ts=4 sts=4 sw=4 et sta ai
set tabstop=4
set softtabstop=4
set shiftwidth=4
set expandtab
set smarttab
set autoindent

" set is hls
set incsearch
set hlsearch

" leader is \ by default
" let mapleader=","
" inoremap jk <esc>
nnoremap <leader><space> :nohlsearch<CR>

" set fen fdls=10 fdn=10 fdm=indent
set foldenable
set foldlevelstart=10
set foldnestmax=10
set foldmethod=indent
nnoremap <space> za

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

" let &cc="80,".join(range(100,999),",")

" map <f4> :!time python %
" map <f5> :!time python %<cr>

" if has("autocmd")
" 	augroup templates
" 		autocmd BufNewFile *.c 0r ~/.vim/templates/skeleton.c
" 	augroup END
" endif
