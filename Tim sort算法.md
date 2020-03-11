# Tim Sort

https://en.wikipedia.org/wiki/Timsort

Timsort 是一种混合稳定的排序算法，源自合并排序和插入排序，旨在较好地处理真实世界中各种各样的数据。它使用了 Peter Mcllroy 的"乐观排序和信息理论上复杂性"中的技术，参见 第四届年度ACM-SIAM离散算法研讨会论文集，第467-474页，1993年。 它由 Tim Peters 在2002年实现，并应用于 Python编程语言。该算法通过查找已经排好序的数据子序列，在此基础上对剩余部分更有效地排序。 该算法通过不断地将特定子序列（称为一个 run ）与现有的 run 合并，直到满足某些条件为止来达成的更有效的排序。 从 2.3 版本起，Timsort 一直是 Python 的标准排序算法。 它还被 Java SE7, Android platform, GNU Octave, 谷歌浏览器,和 Swift用于对非原始类型的数组排序。

Timsort
分类	排序算法
数据结构	数组
最坏时间复杂度	{\displaystyle O(n\log n)}O(n\log n)
最优时间复杂度	{\displaystyle O(n)}O(n)
平均时间复杂度	{\displaystyle O(n\log n)}O(n\log n)
最坏空间复杂度	{\displaystyle O(n)}O(n)

Python 中使用的 Timsort 算法可以有效地进行多种排序，因为它可以利用数据集中已存在的任何排序。
https://docs.python.org/zh-cn/3/howto/sorting.html


