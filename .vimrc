set ts=4
set sw=4
set nu
set showcmd
set hlsearch
set cursorline

map <f4> :!time python %
map <f5> :!time python %<cr>
map <c-h> <c-w>h
map <c-j> <c-w>j
map <c-k> <c-w>k
map <c-l> <c-w>l

if has("autocmd")
	augroup templates
		autocmd BufNewFile *.c 0r ~/.vim/templates/skeleton.c
	augroup END
endif
