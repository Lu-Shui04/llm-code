def read_file(file_path):
    try:
        with open(file_path,"r",
                  encoding="utf-8") as f:
            lines=f.readlines()
            for line in lines:
                print(line.strip())
    except Exception as e:
        print("发现错误：",e)

def write_file(file_path,content):
    try:
        with open(file_path,"a",
                encoding="utf-8") as f:
            f.write("\n" + "\n".join(content.split("，")))
    except Exception as e:
        print("发现错误：",e)


if __name__=="__main__":
    # read_file("day09/小米.txt")
    write_file("day09/小米.txt","""小米是一家中国的
               科技公司，成立于2010年，总部
               位于北京。小米以其智能手机、
               智能家居设备和互联网服务而闻名。
               小米的产品以高性价比和创新设计
               著称，深受消费者喜爱。除了智能
               手机，小米还生产智能电视、智能
               手环、智能音箱等多种智能设备。
               小米在全球范围内拥有庞大的用户
               群体，并且在多个国家和地区设有
               分支机构。""")
    read_file("day09/小米.txt")