from pfmaudita.pfmaudita_ui import Ui_ControlTSR

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QTableWidgetItem

from PyQt5.QtGui import QColor

import sys

import traceback

 

from datetime import date

from datetime import timedelta

from Funciones.conversiones import fcia_chr

from Farmacia.EmpleadoFactory import EmpleadoFactory

from Farmacia.Caja import Caja

from pfmaudita.audita import get_mov, get_faltantes, get_ctacte_personal, get_cajas_fcia, get_tjt, aplica_faltantes, \

    reporte_faltantes_nempa

from pandas import DataFrame, set_option, options

# pip install setuptools==44.0.0

# agregar en spect hiddenimports=['pkg_resources.py2_warn']

from Funciones.parametros import leer_ini

from os import path

from AccesoDatos.MySQL import MySQL

import infocps.config as cf

from pfmaudita.resumen import card_empleado,header,foot

from Funciones.mail import send_mail

from Funciones.fechas import rango_fec_personal

set_option('display.max_columns', None, 'display.width', 1000, 'display.max_rows', None)

#options.display.float_format = '{:,.2f}'.format

#202

#206

#VER DE SACAR ANULACIONES CON TARJETA

class VentanaAudita(QtWidgets.QMainWindow, Ui_ControlTSR):

    def __init__(self,dir_wrk,dir_suc,dir_foxdi,mails,cf,parent=None):

        self.__dirp9suc = dir_suc

        self.__cf = cf

        self.__mails = mails

        self.__dir_foxdi = dir_foxdi

        self.__dir_wrk = dir_wrk

        self.__mail_contenido = None

        super(VentanaAudita, self).__init__(parent)

        self.setupUi(self)

        self.tab_tbls.currentChanged.connect(self.cambia_tab)

 

        self.btn_buscar.clicked.connect(self.buscar)

        self.btn_exporta.clicked.connect(self.exporta)

        self.btn_aplica_ggral.clicked.connect(self.aplica_faltantes)

        self.btn_envia_mail.clicked.connect(self.envia_mail)

 

 

        self.__operaciones = []

        self.btn_exporta.setDisabled(True)

        self.set_fcias()

        self.set_empleados()

 

        self.dt_desde.setDate(date.today() - timedelta(days=1))

        self.dt_hasta.setDate(date.today())

        self.tab_tbls.setCurrentIndex(0)

        self.cambia_tab(0)

        self.tbl_cajas.horizontalHeader().setVisible(True)

        self.tbl_oper.horizontalHeader().setVisible(True)

 

    def cambia_tab(self,i):

        if i == 0:

            self.label.setText("Desde")

 

            self.dt_desde.setDisplayFormat("dd/MM/yyyy")

            self.chk_gastos.setVisible(True)

            self.chk_retiros.setVisible(True)

            self.btn_exporta.setDisabled(True)

            self.cmb_fcias.setVisible(True)

            self.lbl_farmacia.setVisible(True)

            self.chk_exp_faltante.setVisible(False)

            self.chk_exp_sobrante.setVisible(False)

            self.btn_aplica_ggral.setVisible(False)

            self.dt_hasta.setVisible(True)

            self.label_2.setVisible(True)

            self.btn_envia_mail.setVisible(False)

            self.chk_envia_faltantes.setVisible(False)

 

        elif i == 1:

            self.label.setText("Desde")

            self.dt_desde.setDisplayFormat("dd/MM/yyyy")

            self.chk_gastos.setVisible(False)

            self.chk_retiros.setVisible(False)

            self.btn_exporta.setDisabled(True)

            self.cmb_fcias.setVisible(True)

            self.lbl_farmacia.setVisible(True)

            self.chk_exp_faltante.setVisible(True)

            self.chk_exp_sobrante.setVisible(True)

            self.chk_envia_faltantes.setVisible(True)

            self.chk_envia_faltantes.setChecked(False)

            self.chk_exp_sobrante.setChecked(False)

            self.chk_exp_faltante.setChecked(False)

 

            self.btn_aplica_ggral.setVisible(True)

            self.btn_aplica_ggral.setDisabled(True)

            self.dt_hasta.setVisible(True)

            self.label_2.setVisible(True)

            self.btn_envia_mail.setVisible(False)

            self.chk_envia_faltantes.setVisible(True)

 

        elif i == 2:

            self.label_2.setVisible(False)

            self.chk_envia_faltantes.setVisible(False)

            self.btn_envia_mail.setDisabled(True)

 

            self.dt_desde.setDisplayFormat("MM/yyyy")

            self.label.setText("Periodo")

            self.dt_hasta.setVisible(False)

            self.chk_gastos.setVisible(False)

            self.chk_retiros.setVisible(False)

            self.btn_exporta.setDisabled(True)

            self.cmb_fcias.setVisible(False)

            self.lbl_farmacia.setVisible(False)

            self.chk_exp_faltante.setVisible(False)

            self.chk_exp_sobrante.setVisible(False)

            self.btn_aplica_ggral.setVisible(False)

            self.btn_aplica_ggral.setDisabled(False)

            self.btn_envia_mail.setVisible(True)

            self.chk_envia_faltantes.setVisible(False)

 

        elif i == 3:

            self.label.setText("Desde")

            self.chk_envia_faltantes.setVisible(False)

 

            self.dt_desde.setDisplayFormat("dd/MM/yyyy")

            self.dt_hasta.setVisible(True)

            self.btn_envia_mail.setVisible(False)

 

            #self.cmb_fcias.setVisible(False)

            self.chk_gastos.setVisible(False)

            self.chk_retiros.setVisible(False)

            self.btn_exporta.setDisabled(True)

            self.cmb_fcias.setVisible(True)

            self.lbl_farmacia.setVisible(True)

            self.chk_exp_faltante.setVisible(False)

            self.chk_exp_sobrante.setVisible(False)

            self.btn_aplica_ggral.setVisible(False)

            self.label_2.setVisible(True)

            self.chk_envia_faltantes.setVisible(False)

 

        elif i == 4:

            self.label.setText("Desde")

            self.chk_envia_faltantes.setVisible(False)

 

            self.dt_desde.setDisplayFormat("dd/MM/yyyy")

            self.dt_hasta.setVisible(True)

            self.btn_envia_mail.setVisible(False)

            self.cmb_fcias.setVisible(False)

            self.lbl_farmacia.setVisible(False)

            self.chk_gastos.setVisible(False)

            self.chk_retiros.setVisible(False)

            self.btn_exporta.setDisabled(True)

            self.chk_exp_faltante.setVisible(False)

            self.chk_exp_sobrante.setVisible(False)

            self.btn_aplica_ggral.setVisible(False)

            self.label_2.setVisible(True)

            self.chk_envia_faltantes.setVisible(False)

 

        elif i == 5:

            self.label.setText("Desde")

            self.label_2.setVisible(True)

            self.chk_envia_faltantes.setVisible(False)

            self.dt_desde.setDisplayFormat("dd/MM/yyyy")

            self.dt_hasta.setVisible(True)

            self.cmb_fcias.setVisible(True)

            self.lbl_farmacia.setVisible(True)

            self.chk_gastos.setVisible(False)

            self.chk_retiros.setVisible(False)

            self.btn_exporta.setDisabled(True)

            self.chk_exp_faltante.setVisible(False)

            self.chk_exp_sobrante.setVisible(False)

            self.btn_aplica_ggral.setVisible(False)

            self.btn_envia_mail.setVisible(False)

 

            self.chk_envia_faltantes.setVisible(False)

 

    def envia_mail(self):

        if self.__mail_contenido != None:

            lst_mails = list()

            for m in list(self.__mails.keys()):

                mail = self.__mails[m]

                if isinstance(mail,str):

                    lst_mails.append(mail)

                elif isinstance(mail,list):

                    lst_mails.extend(mail)

            if len(lst_mails) > 0:

                for m in list(set(lst_mails)):

                    send_mail({"from": "cajas@puntofarma.com", "usr": "AKIA4SS3SSKJDFPEH5F6",

                       "smtp_server": "email-smtp.us-east-1.amazonaws.com",

                       "pwd": "BBitHD+ujMdSw+Xo6X3RBge+03DucaFP4L8uFLcehLbd"}, [m], "Faltantes y Ajustes de Cajas",

                      contenido=self.__mail_contenido)

 

    def buscar(self):

        self.btn_exporta.setDisabled(True)

        tab_index = self.tab_tbls.currentIndex()

        self.__fcian = self.cmb_fcias.currentData()

 

        fec_desde = self.dt_desde.date()

        fec_hasta = self.dt_hasta.date()

        if self.__fcian != 99:

            self.txt_ultnint.setText(Caja.get_ultima_act(self.__fcian,self.__dirp9suc))

        else:

            self.txt_ultnint.setText(Caja.get_ultima_act(1,self.__dirp9suc))

 

        fec_desde_vfp = "DATE(" + str(fec_desde.getDate()[0]) + "," + str(fec_desde.getDate()[1]) + "," + str(

            fec_desde.getDate()[2]) + ")"

        fec_hasta_vfp = "DATE(" + str(fec_hasta.getDate()[0]) + "," + str(fec_hasta.getDate()[1]) + "," + str(

            fec_hasta.getDate()[2]) + ")"

        fec_mysql_desde = str(fec_desde.getDate()[0])+"-"+str(fec_desde.getDate()[1]).zfill(2)+"-"+str(fec_desde.getDate()[2]).zfill(2)

        fec_mysql_hasta = str(fec_hasta.getDate()[0])+"-"+str(fec_hasta.getDate()[1]).zfill(2)+"-"+str(fec_hasta.getDate()[2]).zfill(2)

 

        if tab_index == 0:

            self.busca_mov(fec_mysql_desde,fec_mysql_hasta)

        elif tab_index == 1:

            self.busca_faltantes(fec_mysql_desde,fec_mysql_hasta)

 

          #  self.busca_faltantes(fec_desde_vfp,fec_hasta_vfp)

        elif tab_index == 2:

            self.busca_faltantes_nempa(fec_desde)

        elif tab_index == 3:

            self.busca_cajas(fec_desde_vfp,fec_hasta_vfp)

        elif tab_index == 4:

            self.busca_consumos(fec_desde_vfp,fec_hasta_vfp)

        elif tab_index == 5:

            self.busca_tarjetas(fec_desde_vfp,fec_hasta_vfp)

 

 

    def busca_mov(self, fec_desde, fec_hasta):

        self.__operaciones = []

        tops = []

        totp9 = 0

        tot_tsr=0

        if self.chk_gastos.isChecked():

            tops.append("203")

        if self.chk_retiros.isChecked():

            tops.append("201")

        try:

           if self.__fcian == 99:

                arr_fcias = list(range(1, 28))

                arr_fcias.remove(2)

                arr_fcias.remove(17)

                for fcia in arr_fcias:

                    ops = get_mov(self.__cf, fcia, fec_desde, fec_hasta, tops)

 

                    self.__operaciones.extend(ops["datos"])

                    totp9 += ops["totp9"]

                    tot_tsr += ops["tot_tsr"]

            else:

                ops = get_mov(self.__cf, self.__fcian, fec_desde, fec_hasta, tops)

                self.__operaciones.extend(ops["datos"])

                totp9 = ops["totp9"]

                tot_tsr = ops["tot_tsr"]

 

            self.txt_totalp9.setText(str(round(totp9,2)))

            self.txt_totaltsr.setText(str(round(tot_tsr,2)))

            if len(self.__operaciones) > 0:

                self.btn_exporta.setDisabled(False)

                self.tbl_oper.setRowCount(len(self.__operaciones))

                for indic, r in enumerate(self.__operaciones):

                    reg = self.__operaciones[indic]

                    for ind, col in enumerate(reg.values()):

                        if str(col).strip() == "nan":

                            col = ""

                        self.tbl_oper.setItem(indic, ind, QTableWidgetItem(str(col)))

                self.tbl_oper.resizeRowsToContents()

            else:

                self.tbl_oper.setRowCount(0)

        except Exception as err:

            traceback.print_exc()

 

            print(err)

 

    def busca_faltantes(self,fec_desde,fec_hasta):

        self.__operaciones = []

        lista_ce = self.__empleados

        exporta = {"faltante": self.chk_exp_faltante.isChecked(), "sobrante": self.chk_exp_sobrante.isChecked(), "mails": self.chk_envia_faltantes.isChecked()}

        try:

            if self.__fcian == 99:

                arr_fcias = list(range(1, 28))

                arr_fcias.append(31)

                arr_fcias.remove(2)

                arr_fcias.remove(17)

                for fcia in arr_fcias:

                    ops = get_faltantes(self.__cf, self.__dir_foxdi, lista_ce, fec_desde, fec_hasta, fcia,

                                        exporta, self.__mails)

 

                    #  ops = get_faltantes(self.__dirp9suc,self.__dir_foxdi,lista_ce,fec_desde, fec_hasta, fcia,exporta,self.__mails)

                    self.__operaciones.extend(ops["datos"])

            else:

                ops = get_faltantes(self.__cf,self.__dir_foxdi,lista_ce,fec_desde, fec_hasta, self.__fcian,exporta,self.__mails)

 

               # ops = get_faltantes(self.__dirp9suc,self.__dir_foxdi,lista_ce,fec_desde, fec_hasta, self.__fcian,exporta,self.__mails)

                self.__operaciones = ops["datos"]

            if len(self.__operaciones) > 0:

                self.btn_exporta.setDisabled(False)

                self.btn_aplica_ggral.setDisabled(False)

                self.tbl_faltantes.setRowCount(len(self.__operaciones))

                for indic, r in enumerate(self.__operaciones):

                    reg = self.__operaciones[indic]

                    for ind, col in enumerate(reg.values()):

                        if str(col).strip() == "nan":

                            col = ""

                        item = QTableWidgetItem(str(col))

                        if ind in (6,7,8,9):

                            if type(col) in (float,int) and col < 0:

                                item.setForeground(QColor(255,0,0))

                            elif type(col) in (float,int) and col > 0:

                                item.setForeground(QColor(0,128,0))

 

                        self.tbl_faltantes.setItem(indic, ind, item)

                self.tbl_faltantes.resizeRowsToContents()

            else:

                self.tbl_faltantes.setRowCount(0)

        except Exception as err:

            traceback.print_exc()

 

            print(err)

 

    def aplica_faltantes(self):

        if len(self.__operaciones) > 0:

            df_op = DataFrame(self.__operaciones)

            df_faltantes = df_op[df_op["faltante_p9"] <= -100]

            aplica_faltantes(df_faltantes.to_dict(orient="records"),self.__dir_foxdi)

 

    def busca_faltantes_nempa(self,periodo):

        lista_ce = self.__empleados

        lista_empleados = list(map(lambda emp: emp.get_datos(), lista_ce))

 

        periodo = str(periodo.getDate()[1]).zfill(2)+"/"+str(periodo.getDate()[0])

        fechas = rango_fec_personal(periodo)

 

        fec_desde = "DATE(" + fechas["fecha_desde"].strftime("%Y") + "," + fechas["fecha_desde"].strftime("%m") + "," + fechas["fecha_desde"].strftime("%d") + ")"

        fec_hasta = "DATE(" + fechas["fecha_hasta"].strftime("%Y") + "," + fechas["fecha_hasta"].strftime("%m") + "," + fechas["fecha_hasta"].strftime("%d") + ")"

 

        dct_faltantes = reporte_faltantes_nempa(self.__dir_foxdi, lista_empleados, fec_desde,fec_hasta)

        self.__operaciones = dct_faltantes["data_table"]

        if len(self.__operaciones) > 0:

            self.btn_exporta.setDisabled(False)

            self.tbl_ajustes_faltantes.setRowCount(len(self.__operaciones))

            for indic, r in enumerate(self.__operaciones):

                reg = self.__operaciones[indic]

                for ind, col in enumerate(reg.values()):

                    if str(col).strip() == "nan":

                        col = ""

                    item = QTableWidgetItem(str(col))

                    self.tbl_ajustes_faltantes.setItem(indic, ind, item)

            self.tbl_ajustes_faltantes.resizeRowsToContents()

        else:

            self.tbl_ajustes_faltantes.setRowCount(0)

        print("paso")

        lst_mov_caj = dct_faltantes["data_faltantes"]

        det_mov_emp = list()

        str_reporte = header

        for emp in dct_faltantes["data_emp"]:

            print(emp)

            empleado = list(filter(lambda reg: str(reg["ncct"]).strip() == emp,lista_empleados))

            lst_mov = list(filter(lambda mov: mov["ce"] == emp,lst_mov_caj))

            total = 0

            for mov in lst_mov:

                total+= mov["valor"]

            str_reporte+=card_empleado(empleado[0], lst_mov,total)

        str_reporte+=foot

        self.__mail_contenido = str_reporte

        self.btn_envia_mail.setDisabled(False)

 

    def busca_consumos(self,fec_desde,fec_hasta):

        try:

            consumos = get_ctacte_personal(self.__dir_wrk,self.__dirp9suc, self.__dir_foxdi, fec_desde, fec_hasta, self.__empleados)

            self.__operaciones = []

            self.__consumo_emp = []

            self.__operaciones.extend(consumos["total"])

            if len(self.__operaciones) > 0:

                self.__consumo_emp = consumos["empleados"]

                self.btn_exporta.setDisabled(False)

                self.tbl_cc_per.setRowCount(len(self.__operaciones))

 

                for indic, r in enumerate(self.__operaciones):

                    reg = self.__operaciones[indic]

                    for ind, col in enumerate(reg.values()):

                        if str(col).strip() == "nan":

                            col = ""

                        self.tbl_cc_per.setItem(indic, ind, QTableWidgetItem(str(col)))

                self.tbl_cc_per.resizeRowsToContents()

                self.btn_exporta.setDisabled(False)

 

            else:

                self.tbl_cc_per.setRowCount(0)

 

        except Exception as err:

            traceback.print_exc()

 

            print(err)

 

    def busca_cajas(self,fec_desde,fec_hasta):

        self.__operaciones = []

        try:

            if self.__fcian == 99:

                arr_fcias = list(range(1, 28))

                arr_fcias.remove(2)

                arr_fcias.remove(17)

                for fcia in arr_fcias:

                    ops = get_cajas_fcia(self.__dirp9suc,fec_desde, fec_hasta, fcia)

                   self.__operaciones.extend(ops["datos"])

            else:

                ops = get_cajas_fcia(self.__dirp9suc,fec_desde, fec_hasta, self.__fcian)

                self.__operaciones = ops["datos"]

            if len(self.__operaciones) > 0:

                self.btn_exporta.setDisabled(False)

                self.tbl_cajas.setRowCount(len(self.__operaciones))

                for indic, r in enumerate(self.__operaciones):

                    reg = self.__operaciones[indic]

                    for ind, col in enumerate(reg.values()):

                        if str(col).strip() == "nan":

                            col = ""

                        self.tbl_cajas.setItem(indic, ind, QTableWidgetItem(str(col)))

                self.tbl_cajas.resizeRowsToContents()

            else:

                self.tbl_cajas.setRowCount(0)

        except Exception as err:

            traceback.print_exc()

 

            print(err)

 

    def busca_tarjetas(self,fec_desde,fec_hasta):

        my_data = MySQL.conecto(cf.ip_srv, cf.usr, cf.pwd, "INFOTJT1") #base de cuentas drg y proveedores

 

        self.__operaciones = []

        try:

            if self.__fcian == 99:

                arr_fcias = list(range(1, 28))

                arr_fcias.remove(2)

                arr_fcias.remove(17)

                for fcia in arr_fcias:

                    ops = get_tjt(self.__dirp9suc,my_data, fec_desde, fec_hasta, fcia)

                    self.__operaciones.extend(ops["datos"])

            else:

                ops = get_tjt(self.__dirp9suc,my_data,fec_desde, fec_hasta, self.__fcian)

                self.__operaciones = ops["datos"]

        except Exception as err:

            traceback.print_exc()

 

            pass

      #  print(self.__operaciones)

 

 

 

    def exporta(self):

        try:

            datos = DataFrame(self.__operaciones)

            tab_index = self.tab_tbls.currentIndex()

            if tab_index == 0:

                export_file = "control_sobres-"+fcia_chr(self.__fcian)

            elif tab_index == 1:

                export_file = "detalle_faltantes_sobrantes-"+fcia_chr(self.__fcian)

            elif tab_index == 2:

                export_file = "detalle_faltantes_ajustes-"+fcia_chr(self.__fcian)

                print(export_file)

            elif tab_index == 3:

                fec_desde = self.dt_desde.date()

                fec_hasta = self.dt_hasta.date()

                fec_des = str(fec_desde.getDate()[0])+"-"+str(fec_desde.getDate()[1])+"-"+str(fec_desde.getDate()[2])

                fec_has = str(fec_hasta.getDate()[0])+"-"+str(fec_hasta.getDate()[1])+"-"+str(fec_hasta.getDate()[2])

                export_file = "resumen_consumos_"+fec_des+"_"+fec_has

                if len(self.__consumo_emp) > 0:

                    df_consumos = DataFrame(self.__consumo_emp)

                    df_consumos.to_excel("C:/t1/detalle_consumos" + fec_des+"_"+fec_has + ".xlsx", index=False)

 

                    #for ncct in df_consumos["ncct"].values:

                    #    df_emp = df_consumos[df_consumos["ncct"] == ncct]

 

                        #print(df_emp)

                     #   df_emp.to_excel("C:/t/resumen_consumos_" +str(df_emp["ncct"].min()) + ".xlsx", index=False)

 

            datos.to_excel("C:/t1/"+export_file+".xlsx",index=False)

        except Exception as err:

            traceback.print_exc()

 

           print(err)

 

    def set_fcias(self):

        arr_fcias = list(range(1, 28))

        arr_fcias.remove(2)

        arr_fcias.remove(17)

        arr_fcias.append(31)

 

        self.cmb_fcias.addItem("Todas",99)

        for fc in arr_fcias:

            self.cmb_fcias.addItem(fcia_chr(fc), fc)

 

    def set_empleados(self):

        empleados = EmpleadoFactory()

        self.__empleados = empleados.lista(self.__dir_foxdi)

 

 

from PyQt5.QtWidgets import QMainWindow, QPushButton,QMessageBox

from PyQt5.QtCore import QSize

 

 

class MensajeError(QMainWindow):

    def __init__(self,mensaje):

        QMainWindow.__init__(self)

 

      #  self.setMinimumSize(QSize(300, 200))

      #  self.setWindowTitle("ERROR!!!!!!!!!!!!!")

        QMessageBox.about(self, "ERROR", mensaje)

 

 

 

if _name_ == '__main__':

    dir_par = "C:/idi/control.json"

    try:

        if path.exists(dir_par):

            params = leer_ini(dir_par, ["dir_p9wrk","dir_p9suc","dir_foxdi","mails","cf"])

        app = QApplication(sys.argv)

        form = VentanaAudita(params["dir_p9wrk"],params["dir_p9suc"],params["dir_foxdi"],params["mails"],params["cf"])

        form.show()

        sys.exit(app.exec_())

    except Exception as err:

        ap = QtWidgets.QApplication(sys.argv)

        mainWin = MensajeError(str(err))

        ap.exec_()

        traceback.print_exc()

        print(err)

       # input()

