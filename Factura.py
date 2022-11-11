ListaProductosMenu=[
        ['#CODIGO  PRODUCTO          PRECIO'],
        ['#1       Hamburguesa       10000 >>>'],
        ['#2       Perro Caliente    7000 >>>'],
        ['#3       Pizza             6000 >>>'],
        ['#4       Sandwich          5000 >>>'],
        ['#5       CocaCola          2500 >>>'],
        ['#6       Pepsi             1000 >>>'],
        ['#7       Ginger            3000 >>>'],
        ['#8       Awa de uwu        ∞    >>>']
    ]
class Tienda:
  def __init__(self):
    self.pedidofactura = ([])
    self.pedido = ([])
    import qrcode
    img = qrcode.make("Bienvenido Gracias por escanear nuestro QR, Visita mi pagina de GitHub dando click en el siguiente enlace : https://github.com/JhonTova")
    f = open("QR.png","wb")
    img.save(f)
    self.Menu()
  def log(self):
    contraseña = int(input("Digite su contraseña"))
    if contraseña == 123 :
      self.Menu()
    else:
      print("Error saliendo de el sistema")
      exit()
  def Menu(self):
    menu=[
        ['========Restaurante========'],
        ['1. Ver Menu >>>'],
        ['2. Pedir Productos >>>'],
        ['3. Generar Factura >>>'],
        ['4. salir >>>']
    ]
    for x in range(5):
     print(menu[x][0])
    opcion=int(input("Seleccione Una Opcion <<<"))
    if opcion==1:
      self.MostrarMenu()
    elif opcion==2:
      self.AgregarProductos()
    elif opcion==3:
      self.GenerarFactura()
    elif opcion==4:
      print("Saliendo ...")
      exit()
  def MostrarMenu(self):
    for x in range(9):
     print(ListaProductosMenu[x][0])
    self.Menu()
  def AgregarProductos(self):
    print("1 = Agregar")
    print("2 = Eliminar")
    print("3 = Ver Pedido")
    print("4 = Ir al menu principal")
    opcion = int(input("Digite su desicion"))
    if  opcion == 1:
        producto = int(input("Digite el codigo de el producto a agregar"))
        if producto == 1:
            self.pedidofactura.append("Hamburguesa = 10000")
            self.pedido.append(10000)
            self.AgregarProductos()
        if producto == 2:
            self.pedidofactura.append("Perro Caliente = 7000")
            self.pedido.append(7000)
            self.AgregarProductos()
        if producto == 3:
            self.pedidofactura.append("Pizza = 6000")
            self.pedido.append(6000)
            self.AgregarProductos()
        if producto == 4:
            self.pedidofactura.append("Sandwich = 5000")
            self.pedido.append(5000)
            self.AgregarProductos()
        if producto == 5:
            self.pedidofactura.append("CocaCola = 2500")
            self.pedido.append(2500)
            self.AgregarProductos()
        if producto == 6:
            self.pedidofactura.append("Pepsi = 1000")
            self.pedido.append(1000)
            self.AgregarProductos()
        if producto == 7:
            self.pedidofactura.append("Ginger = 3000")
            self.pedido.append(3000)
            self.AgregarProductos()
        if producto == 8:
            self.pedidofactura.append("Awa = 0")
            self.pedido.append(0)
            self.AgregarProductos()
        if producto > 8:
            print("Producto No Encontrado")
            print("Regresando al menu principal ....")
            self.Menu()
    if  opcion == 2:
        borrar = input("Digite el nombre de el producto a eliminar")
        self.pedidofactura.remove(borrar)
        self.pedido.remove(borrar)
        self.AgregarProductos()
    if  opcion == 3:
        print(self.pedidofactura)
        self.AgregarProductos()
    if opcion == 4:
        self.Menu()
  def GenerarFactura(self):
    import datetime
    import climage
    from reportlab.pdfgen import canvas
    print("1 = Efectivo")
    print("2 = Tarjeta")
    FormaPago = int(input("Digite su forma de pago"))
    if FormaPago == 1:
      FormaPago = ("Efectivo")
    else:
      FormaPago = ("Tarjeta")
    print("DONUCOL S.A")
    print("NIT: 860508791-1")
    print("Agente responsable de IVA. CIIU 1081")
    print("Agente retenedor de ICA")
    print("TEL : 3207843347")
    print("servicioalcliente@dunkindonuts.com.co")
    print("TERMINAL SALTRE")
    print("DG 23 69 55 LC 126")
    print("Aut. DIAN 18764027319797 FEC 01/04/2022")
    print("Desde JK - 33449 HASTA JK 1000")
    print("DCTO/EQUIVALENTE POS: JK -52357")
    print("===================")
    delta = datetime.timedelta(days=365)
    fecha1 = datetime.date.today()
    vigencia = delta + fecha1
    print("Vigencia Hasta", vigencia)
    Fecha = datetime.datetime.now()
    FechaActual = datetime.datetime.strftime(Fecha, "%d/%m/%Y")
    HoraActual = datetime.datetime.strftime(Fecha, "%H:%M:%S")
    print("FECHA : ", FechaActual," HORA : ",HoraActual)
    print("====================")
    print("Lista de productos a pagar")
    print(self.pedidofactura)
    TotalSuma = sum(self.pedido)
    TotalIva = TotalSuma * 0.19
    TotalPagar = TotalIva + TotalSuma
    print("La suma de todos su productos equivale a : ",TotalSuma,"$")
    print("====================")
    print("Mas ",TotalIva,"$ de IVA")
    print("Total a pagar = ",TotalPagar)
    print("====================")
    print("Forma de pago : ",FormaPago)
    print("====================")
    print("GRACIAS POR SU COMPRA!")
    print("Visita nuestra pagina web")
    print("Escaneando el siguiente QR")
    imagenqr = climage.convert("QR.png", is_unicode = False, is_truecolor = False, is_256color = True, is_16color = False, is_8color = False, width = 20, palette = "default")
    print(imagenqr)
    print("===================")
    print("Tiquete POS impreso por una impresora")
    print("Desarrollado por Jhon Tovar")
    print("====================")
    print("Si requiere Factura electronica de venta")
    print("Solicitela en el siguiente correo")
    print("SOLICITESUDFE@DUNKINDONUTS.COM.CO")
    print("Digite su contraseña")
    pdf = canvas.Canvas("Factura.pdf")
    pdf.drawString(250, 800,"DONUCOL S.A")
    pdf.drawString(200, 780, "==============================")
    pdf.drawString(200, 760, "NIT: 860508791-1")
    pdf.drawString(200, 740, "Agente responsable de IVA. CIIU 1081")
    pdf.drawString(200, 720, "Agente retenedor de ICA")
    pdf.drawString(200, 700, "TEL : 3207843347")
    pdf.drawString(200, 680, "servicioalcliente@dunkin.com.co")
    pdf.drawString(200, 660, "TERMINAL SALITRE")
    pdf.drawString(200, 640, "DG 23 69 55 LC 126")
    pdf.drawString(200, 620, "Aut. DIAN 18764027319797 FEC 01/04/2022")
    pdf.drawString(200, 600, "Desde JK - 33449 HASTA JK 1000")
    pdf.drawString(200, 580, "DCTO/EQUIVALENTE POS: JK -52357")
    pdf.drawString(200, 560, "==============================")
    pdf.drawString(200, 540, "Vigencia Hasta " f"{vigencia}")
    pdf.drawString(200, 520, "FECHA : "+ FechaActual+" HORA : "+ HoraActual)
    pdf.drawString(200, 500, "==============================")
    pdf.drawString(200, 480, "Lista de productos a pagar")
    pdf.drawString(200, 460, f"{self.pedidofactura}")
    pdf.drawString(200, 440, "La suma de todos su productos equivale a : "f"{TotalSuma}""$")
    pdf.drawString(200, 420, "==============================")
    pdf.drawString(200, 400, "Mas "f"{TotalIva}""$ de IVA")
    pdf.drawString(200, 380, "Total Pagar : "f"{TotalPagar}")
    pdf.drawString(200, 360, "==============================")
    pdf.drawString(200, 340, "Forma de pago : "+ FormaPago)
    pdf.drawString(200, 320, "==============================")
    pdf.drawString(200, 300, "GRACIAS POR SU COMPRA!")
    pdf.drawString(200, 280, "Visita nuestra pagina web")
    pdf.drawString(200, 260, "Escaneando el siguiente QR")
    pdf.drawImage("QR.png", 250,155, width=100, height=100)
    pdf.drawString(200, 140, "==============================")
    pdf.drawString(200, 120, "Tiquete POS impreso por una impresora")
    pdf.drawString(200, 100, "Desarrollado por Jhon Tovar")
    pdf.drawString(200, 80, "==============================")
    pdf.drawString(200, 60, "Si requiere Factura electronica de venta")
    pdf.drawString(200, 20, "SOLICITESUDFE@DUNKINDONUTS.COM.CO")
    pdf.drawString(200, 40, "Solicitela en el siguiente correo")
    pdf.save()
    self.pedido.clear()
    self.pedidofactura.clear()
    self.Menu()