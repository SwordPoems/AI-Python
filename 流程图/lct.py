from diagrams import Diagram, Cluster, Node

# 创建流程图
with Diagram("ERP 系统流程图", show=False):
    with Cluster("供应商"):
        supplier_info = Node("提供商品信息", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/computer.png")
        supplier_order = Node("接收订单并生产发货", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/computer.png")
        supplier_notification = Node("发送发货通知", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/computer.png")
        supplier_payment = Node("接收支付信息", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/computer.png")

    with Cluster("ERP 系统"):
        erp_receive_info = Node("接收并存储", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_send_order = Node("发送采购订单", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_receive_notification = Node("接收发货通知并发送给客户", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_order_confirmation = Node("接收订单并确认", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_payment_confirmation = Node("接收支付信息并确认", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_send_customer_notification = Node("发送订单确认信息", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")
        erp_send_shipping_notification = Node("发送发货通知给客户", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/server.png")

    with Cluster("客户"):
        customer_order = Node("下订单", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/mobile.png")
        customer_payment = Node("进行支付", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/mobile.png")

    with Cluster("管理员"):
        admin_maintenance = Node("日常操作和维护", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/monitor.png")
        admin_tasks = Node("系统配置、故障排除等任务", icon="https://raw.githubusercontent.com/mingrammer/diagrams/master/resources/generic/monitor.png")

    # 连接供应商流程
    supplier_info >> erp_receive_info
    erp_receive_info >> erp_send_order
    erp_send_order >> supplier_order
    supplier_order >> supplier_notification
    supplier_notification >> erp_receive_notification
    erp_receive_notification >> supplier_payment

    # 连接客户流程
    customer_order >> erp_order_confirmation
    erp_order_confirmation >> customer_payment
    customer_payment >> erp_payment_confirmation
    erp_payment_confirmation >> erp_send_customer_notification
    erp_send_customer_notification >> erp_send_shipping_notification

    # 连接管理员流程
    admin_maintenance >> admin_tasks