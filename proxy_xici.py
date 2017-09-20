from lxml import etree
import requests
import time

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"
}
#代理ip地址爬去方法
ip_lists = []
def downLoad_ip(urls):
    time.sleep(2)
    wb_html = requests.get(urls,headers=headers)
    wb_data= etree.HTML(wb_html.text)
    ips = wb_data.xpath("//table[@id='ip_list']/tr/td[2]/text()")
    ports = wb_data.xpath("//table[@id='ip_list']/tr/td[3]/text()")
    for ip,port in zip(ips,ports):
        ip_list = "https:{0}:{1}".format(ip,port)
        ip_lists.append(ip_list)

#打印代理ip地址
def ip_List():
    for ip in ip_lists:
        print(ip)

#生成url地址（翻页）
def downLoad_urls(pages):
    for i in range(1,pages+1):
        url = "http://www.xicidaili.com/wn/{0}".format(i)
        downLoad_ip(url)


if __name__ == '__main__':
    #爬去多少页ip的代理地址
    downLoad_urls(10)