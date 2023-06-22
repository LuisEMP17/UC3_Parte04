from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
layout = """
    <h1> Proyecto Web (LP3) | Luis Montes Palacios </h1>
    <hr/>
    <ul>
        <li>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/saludo"> Mensaje de Saludo</a>
        </li>
        <li>
            <a href="/rango"> Mostrar Números [a,b]</a>
        </li>
        <li>
            <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
        </li>
    </ul>
    <hr/>
"""
def index(request):
    cursos = [ 'Ingenieria de Requerimientos',
                    'Dibujo Técnico',
                    'Gestión de Proceso de Negocio',
                    'Algoritmos de Computación Gráfica',
                    'Dinámica de Sistemas',
                    'Microprocesadores',
                    'Legislación informática',]

    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'cursos': cursos
})

def examen(request):
    return render(request,'examen.html',{
})
def rango(request):
    return render(request, 'rango.html', 
    {}
)

