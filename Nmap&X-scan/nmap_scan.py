import nmap

# 初始化 Nmap 扫描器
nm = nmap.PortScanner()

# IP 地址和其他参数
TARGET_IP = "127.0.0.1"  # 目标主机的 IP 地址
PING_SCAN = True  # 是否进行主机发现扫描 (等同于 -sP)
PORTS_TO_SCAN = "21,23,53,80"  # 要扫描的端口范围
OS_SCAN = True  # 是否进行操作系统扫描 (等同于 -O)
DECOYS = "1.1.1.1,2.2.2.2,3.3.3.3"  # 欺骗扫描时使用的虚假源 IP 地址列表

def scan_host(ip):
    """扫描目标主机的基本信息"""
    print(f"正在扫描主机: {ip}")
    
    # 执行 Nmap 主机发现扫描 (-sn 等同于 -sP)
    nm.scan(hosts=ip, arguments='-sn')
    
    for host in nm.all_hosts():
        if nm[host].state() == 'up':
            print(f"主机 {host} 是活动的")
            print(f"主机名: {nm[host].hostname()}")
            print(f"MAC 地址: {nm[host]['addresses'].get('mac', '未知')}")
            print(f"厂商: {nm[host]['vendor'].get(nm[host]['addresses'].get('mac'), '未知')}")
        else:
            print(f"主机 {host} 不是活动的")

def scan_ports(ip, ports):
    """扫描指定端口"""
    print(f"正在扫描 {ip} 的端口: {ports}")
    
    # 执行 Nmap 端口扫描 (-p 指定端口范围, -sS 使用 SYN 扫描, -v 详细模式)
    nm.scan(hosts=ip, ports=ports, arguments='-sS -v')
    
    for proto in nm[ip].all_protocols():
        print(f"协议: {proto}")
        
        lport = nm[ip][proto].keys()
        for port in lport:
            state = nm[ip][proto][port]['state']
            name = nm[ip][proto][port]['name']
            product = nm[ip][proto][port].get('product', '未知')
            version = nm[ip][proto][port].get('version', '未知')
            print(f"端口: {port}\t状态: {state}\t服务: {name}\t产品: {product}\t版本: {version}")

def scan_os(ip):
    """扫描目标主机的操作系统信息"""
    print(f"正在扫描 {ip} 的操作系统信息")
    
    # 执行 Nmap OS 检测 (-O, -sS 使用 SYN 扫描, -v 详细模式)
    nm.scan(hosts=ip, arguments='-sS -O -v')
    
    if 'osclass' in nm[ip]:
        for osclass in nm[ip]['osclass']:
            print(f"操作系统: {osclass['osfamily']} {osclass['osgen']}")
            print(f"类型: {osclass['type']}")
            print(f"CPE: {osclass['cpe']}")
    elif 'osmatch' in nm[ip]:
        for osmatch in nm[ip]['osmatch']:
            print(f"可能的操作系统: {osmatch['name']}")
            print(f"准确性: {osmatch['accuracy']}")
    else:
        print("无法检测到操作系统信息")

def spoof_scan(ip, decoys):
    """欺骗扫描，使用虚假的源 IP 地址"""
    print(f"正在对 {ip} 进行欺骗扫描，使用虚假源 IP: {decoys}")
    
    # 执行 Nmap 欺骗扫描 (-D 指定虚假源 IP, -sT 使用 TCP connect() 扫描, -v 详细模式)
    nm.scan(hosts=ip, arguments=f"-D {decoys} -sT -v")
    
    for proto in nm[ip].all_protocols():
        print(f"协议: {proto}")
        
        lport = nm[ip][proto].keys()
        for port in lport:
            state = nm[ip][proto][port]['state']
            name = nm[ip][proto][port]['name']
            print(f"端口: {port}\t状态: {state}\t服务: {name}")

def main():
    # 扫描主机信息
    if PING_SCAN:
        scan_host(TARGET_IP)
    
    # 扫描指定端口
    if PORTS_TO_SCAN:
        scan_ports(TARGET_IP, PORTS_TO_SCAN)
    
    # 如果指定了 --os 参数，则进行操作系统扫描
    if OS_SCAN:
        scan_os(TARGET_IP)
    
    # 如果指定了 --spoof 参数，则进行欺骗扫描
    if DECOYS:
        spoof_scan(TARGET_IP, DECOYS)

if __name__ == "__main__":
    main()