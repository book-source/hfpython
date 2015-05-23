# Q: 列表项目去重


# A1： 使用循环
unique_james = []

for each_t in james:
  if each_t not in unique_james:
    unique_james.append(each_t)

# A2： 使用集合set

unique_james = set(james)
