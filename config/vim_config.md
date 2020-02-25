## Vim config

### Tab键设置为4个空格

修改全局Vim配置
> vim /etc/vim/vimrc

修改当前用户Vim配置
> vim ~/.vimrc

ts:  (ts是tabstop的缩写) 一个tab显示多少个空格的长度，vim默认8。

autoindent:  前行有缩进时，后续的新行将会自动缩进到相同的位置。

softtabstop:  编辑模式的时候按退格键的时候退回缩进的长度。

shiftwidth:  每一级缩进的长度，一般设置成跟 softtabstop 一样。

expandtab:  缩进用空格来表示。

noexpandtab:  缩进用制表符表示。

注：expandtab / noexpandtab 二选一。

```
set ts=4    
set autoindent
set softtabstop=4
set shiftwidth=4
set expandtab
```
