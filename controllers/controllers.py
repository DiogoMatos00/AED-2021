from aed_ds.singly_linked_list import SinglyLinkedList
import ctypes
from aed_ds.open_hash_table import OpenHashTable
from models.data import Data
from models.cliente import Cliente
from aed_ds.singly_linked_list_iterator import Iterator
from models.familia import Familia
from models.serie import Serie
from models.episodio import Episodio
from models.temporada import Temporada
from ctypes import py_object
from typing import Callable, MutableSequence
from models.alugg import alug


class Controller:

    def __init__(self) -> None:

        self.Data = None
        self.Clientes = OpenHashTable(100)
        self.Familias = OpenHashTable(100)
        self.Series = OpenHashTable(100)
        self.identificador_cliente = 1
        self.identificador_familia = 1
        self.identificador_serie = 1
        self.ep_alugados = SinglyLinkedList()

    def numero_planos(self, plano):
        if plano == "Standard":
            return 1
        if plano == "Premium":
            return 2
        if plano == "Pack":
            return 3
        if plano == "Cancelado":
            return 4


    def definir_data(self,data):
        if self.Data == None:
            self.Data = data
            return "Data alterada."
        elif data < self.Data:
            return "Data indicada é anterior a atual."
        else:
            self.Data = data
            return "Data alterada."

    def registar_cliente(self, plano, nome):
        if self.Data is None:
               return "Sem data definida."
        else:
            if plano != "Standard" and plano != "Premium":
                return "Plano inexistente."
            else:
                cliente = None
                values = self.Clientes.values()
                it = values.iterator()
                while it.has_next():  
                    cliente = it.get_next()
                    if nome == cliente.get_nome():
                        return "Cliente existente."
                else:
                    obj = Cliente(nome, plano, self.identificador_cliente)
                    self.Clientes.insert(self.identificador_cliente,obj)
                    self.identificador_cliente += 1
                    return "Cliente registado com o identificador " + str(self.identificador_cliente-1) + "."


    def registar_familia(self, nome):
        if self.Data is None:
            return "Sem data definida."
        else:
            familia = None
            values = self.Familias.values()
            it = values.iterator()
            while it.has_next():
                familia = it.get_next()
                if nome == familia.get_nome_familia():
                    return "Familia existente"
            else:
                obj = Familia(nome, self.identificador_familia)
                self.Familias.insert(self.identificador_familia,obj)
                self.identificador_familia +=1
                return "Familia registada com o identificador: " + str(self.identificador_familia-1) + "."

    def registar_serie(self, nome):
        if self.Data is None:
            return "Sem data definida."
        values = self.Series.values()
        it = values.iterator()
        while it.has_next():
            serie = it.get_next()
            if nome == serie.get_nome_serie():
                return "Serie existente."
        else:
            obj = Serie(nome, self.identificador_serie)
            self.Series.insert(self.identificador_serie, obj)
            self.identificador_serie += 1
            return "Serie registada com o identificador: " + str(self.identificador_serie-1) + "."


    def registar_episodio(self, identificador, num_temp, numep, nomeep):
        try:
            serie = self.Series.get(identificador)
            try:
                temporada = serie.num_temp.get(num_temp)
                try:
                    temporada.get(numep)
                    return "Episódio existente."
                except:
                    ep = Episodio(identificador, num_temp, numep, nomeep)
                    temporada.insert(numep, ep)
                    return "Registo efetuado com sucesso."
            except:

                temporada = Temporada(num_temp)

                serie.num_temp.insert(num_temp, temporada)
 
                ep = Episodio(identificador, num_temp, numep, nomeep)

                temporada.num_episodios.insert(numep, ep)

                return "Registo efetuado com sucesso."
        except:
            return "Série inexistente."


    def alterar_plano(self, identificador, plano):
        try:
           cliente = self.Clientes.get(identificador)
           if cliente.get_familia_cliente() != None:
                return "Cliente associado a família."
           else:
                cliente.set_plano(plano)
                return "Plano alterado com sucesso."
        except:
                return "Cliente inexistente."


    def cancelar_plano(self, identificador):
        try:
            cliente = self.Clientes.get(identificador)
            cliente.set_plano("Cancelado")
            return "Plano cancelado com sucesso."
        except:
            return "Cliente inexistente."

    def associar_cliente_familia(self, identificador_cliente, identificador_familia):
        try:
            cliente = self.Clientes.get(identificador_cliente)
            if cliente.get_familia_cliente() != None:
                return "Cliente associado a outra familia"
            else:
                try:
                    self.Familias.get(identificador_familia)
                    cliente.set_familia_cliente(identificador_familia)
                    cliente.set_plano("Pack")
                    return "Cliente associado com sucesso."
                except:
                    return "Familia inexistente"
        except:
            return "Cliente inexistente"

    def desassociar_cliente_familia(self, identificador_cliente):
        try:
            cliente = self.Clientes.get(identificador_cliente)
            id_familia = cliente.get_familia_cliente()
            if cliente.get_familia_cliente() == None:
                return "Cliente não associado a família."
            else:
                    cliente.set_familia_cliente(None)
                    cliente.set_plano("Cancelado")
                    return "Cliente desassociado com sucesso."
        except:
            return "Cliente inexistente"

    def eliminar_serie_ou_temporada_ou_episodio(self, identificador_serie, Series):   #acabar
        try:
            Series.get(identificador_serie)
            try:
                Series.get_numtemp(identificador_serie)
            except:
                return "Temporada inexistente."
        except:
            return "Série inexistente."

    def eliminar_cliente(self, identificador_cliente):
        try:
            self.Clientes.remove(identificador_cliente)
            return "Cliente eliminado com sucesso."
        except:
            return "Cliente inexistente."

    def listar_clientes(self):
        lista = self.Clientes
        cli = lista.values()
        arr = (ctypes.py_object * cli.size())
        array = arr()
        it = cli.iterator()
        i = 0
        while it.has_next(): #O(n)
            array[i] = it.get_next()
            i += 1
        a = self.quicksort(array, 0, len(array) - 1, self.comp_cliente)
        result = ""
        for i in range (len(a)):
            result += (a[i].get_plano())  + " "
            result += (a[i].get_nome()) + "\n"
        return result

    def listar_familias(self):
        lista = self.Clientes
        cli = lista.values()
        it2 = cli.iterator()
        lista2 = SinglyLinkedList()
        while it2.has_next():
            cliente = it2.get_next()
            if cliente.get_familia_cliente() != None:
                lista2.insert_last(cliente) 
            if lista2 == None:
                return "Sem famílias registadas."
        arr = (ctypes.py_object * lista2.size())
        array = arr()
        it = lista2.iterator()
        i = 0
        while it.has_next(): #O(n)
            array[i] = it.get_next()
            i += 1
        a = self.quicksort(array, 0, len(array) - 1, self.comp_familia)
        result = ""
        for i in range (len(a)):
            result += (self.Familias.get(a[i].get_familia_cliente()).get_nome_familia())  + " "
            result += (a[i].get_nome()) + "\n"
        return result

    def listar_series(self):
        lista = self.Series
        cli = lista.values()
        it2 = cli.iterator()
        lista2 = SinglyLinkedList()
        while it2.has_next():
            serie = it2.get_next()
            if serie.get_nome_serie() != None:
                lista2.insert_last(serie) 
            if lista2 == None:
                return "Sem séries registadas."
        arr = (ctypes.py_object * lista2.size())
        array = arr()
        it = lista2.iterator()
        i = 0
        while it.has_next(): #O(n)
            array[i] = it.get_next()
            i += 1
        a = self.quicksort(array, 0, len(array) - 1, self.comp_series)
        result = ""
        for i in range (len(a)):
            result += (a[i].get_nome_serie()) + "\n"
        return result
            


    def comp_cliente(self, a,b):
        c1 =str(self.numero_planos(a.get_plano())) + a.get_nome().upper() #upper mete tudo em maiuscula
        c2=str(self.numero_planos(b.get_plano())) + b.get_nome().upper()         
        return c1 < c2

    def comp_familia(self, a, b):
        c1 = self.Familias.get(a.get_familia_cliente()).get_nome_familia() + a.get_nome().upper()         
        c2 = self.Familias.get(b.get_familia_cliente()).get_nome_familia() + b.get_nome().upper()         
        return c1 < c2

    def comp_series(self, a, b):
        c1 =str(self.Series.get(a.get_identificador_serie())) + a.get_nome_serie().upper()         
        c2 =str(self.Series.get(b.get_identificador_serie())) + b.get_nome_serie().upper()         
        return c1 < c2

    def quicksort(self, collection: MutableSequence,left_idx: int,right_idx: int,comp: Callable[[int, int], bool]) -> None:
        i: int = left_idx
        j: int = right_idx
        pivot: int = collection[int((i + j) / 2)]
        while i <= j:
            while comp(collection[i], pivot) and i < len(collection):
                i += 1
            while comp(pivot, collection[j]) and j > -1:
                j -= 1
            if i <= j:
                tmp: int = collection[j]
                collection[j] = collection[i]
                collection[i] = tmp
                i += 1
                j -= 1
        if left_idx < j:
            collection = self.quicksort(collection, left_idx, j, comp)
        if i < right_idx:
            collection = self.quicksort(collection, i, right_idx, comp)
        return collection
    
    def eliminar_serie(self, id_s, id_t = 0, id_e = 0):
        try:
            serie = self.Series.get(id_s)
        except:
            return "Série inexistente."

        if id_t == 0:
            self.Series.remove(id_s)
            return "Conteúdo eliminado com sucesso."                

        try:
            temporada = serie.num_temp.get(id_t)
        except:
            return "Temporada inexistente."
        
        if id_e == 0:
            serie.num_temp.remove(id_t)
            return "Conteúdo eliminado com sucesso."   

        try:
            temporada.num_episodios.get(id_e)
        except:
            return "Episódio inexistente."

  
        temporada.num_episodios.remove(id_s)
        return "Conteúdo eliminado com sucesso."

    def alugar_serie(self,num_cliente, num_serie, num_temp, num_episodio):
        try:       
            serie = self.Series.get(num_serie)
        except:
            return "Série inexistente."
            
        try:
            temporada = serie.num_temp.get(num_temp)
        except:
            return "Temporada inexistente."

        if num_episodio != 0:
            try:
                temporada.num_episodios.get(num_episodio)
            except:
                return "Episódio inexistente."

        if num_episodio == 0:  
            serie = self.Series.get(num_serie)
            temporada = serie.num_temp.get(num_temp)
            values = temporada.num_episodios.values()
            it = values.iterator()
            sim = self.ep_alugados.iterator()
            while it.has_next():
                next = it.get_next()
                quero_alugar = alug(num_cliente, num_serie, next, num_temp)
                while sim.has_next():
                    simnext = it.get_next()
                    if simnext.serie_alugada() == quero_alugar.serie_alugada():
                        if simnext.temporada_alugada() == quero_alugar.temporada_alugada():
                            if simnext.episodio_alugada() == quero_alugar.episodio_alugada():
                                continue
                self.ep_alugados.insert_last(quero_alugar)
            return "Conteúdo alugado com sucesso."

        quero_alugar = alug(num_cliente, num_serie, num_episodio, num_temp)

        it = self.ep_alugados.iterator()
        while it.has_next():
            next = it.get_next()
            if next.serie_alugada() == quero_alugar.serie_alugada():
                if next.temporada_alugada() == quero_alugar.temporada_alugada():
                    if next.episodio_alugada() == quero_alugar.episodio_alugada():
                        return "Episódio inexistente."
        
        self.ep_alugados.insert_last(quero_alugar)
        return "Conteúdo alugado com sucesso."