print("="*50)
print(" "*18+"Ai学习进度诊断器")
print("="*50)
day=int(input("你学到第几天了？(1-180):"))
hours_today=float(input("今天学习了多久（小时）:"))
completed_practive=input("今天的练习做完了吗？(y/n):")
felt_difficult=input("今天的内容感觉难吗(y/n):")

print("\n-------诊断报告--------")

#进度分析
if day<=7:
    print("✅️阶段: python 基础入门")
    if day<=3:
        print("""✅️你刚起步,还在建立编程直觉。
              别着急，这阶段最重要的是每天写代码。""")
    else:
        print("✅️第一周过半，应该适应了基本写代码节奏。")
elif day<=30:
    print("✅️阶段: Python 进阶")
elif day<=60:
    print("✅️阶段: Ai 聊天应用开发")
elif day<=120:
    print("✅️阶段: RAG 知识库系统")
elif day<=180:
    print("✅️阶段: AI Agent + 打磨")

#学习时间分析
if hours_today>=2:
    print("⏰️ 今天投入学习充足，注意保护眼睛。")
elif hours_today>=1:
    print("⏰️ 今天时间适中，保持这个节奏。")
elif hours_today>0:
    print("⏰️ 今天时间偏少，哪怕 30 分钟，每天坚持比一次猛学更重要。")
else:
    print("⏰️ 今天还没学？现在开始也不晚！")


#综合建议
if completed_practive=="y" and felt_difficult=="n":
    print("✅️ 状态很好，按计划继续推进。")
elif completed_practive=="y" and felt_difficult=="y":
    print("🤔 练习做完了但感觉难？这是正常的学习曲线。把难点记录下来，明天回顾。")
elif completed_practive=="n" and felt_difficult=="y":
    print("""⚠️ 练习没做完而且感觉难？建议：
          1.回顾一下前面内容
          2.把今天的教程再读一遍
          3.先做最简单的那个练习""")
else:
    print("👊 练习没做完但觉得不难？别偷懒，把练习补上！")

#明天提醒
print("\n-------明天提醒--------")
if day<180:
    print(f"明天是Day {day+1},继续加油！")
    if day%7==0:
        print("明天是新的一个学习周，也是回顾和测验日。")
else:
    print("你已经完成了全部学习 180 天！恭喜！㊗️")

print("\n记住: 编程不是看会的，是写会的。每天都动手写代码。")


