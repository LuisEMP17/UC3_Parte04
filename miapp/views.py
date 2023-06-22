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
    return render(request,'index.html', {
})

def examen(request):
    return render(request,'examen.html',{
})
def rango(request):
    return render(request, 'rango.html', 
    {}
)

