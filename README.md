# weather-data-analysis
Este repositorio contiene un cuaderno jupiter donde se documenta el tratamiento
de los datos de la API de [OpenWeather](https://openweathermap.org/).

### Entorno de ejecución
Para usar este cuaderno es necesario disponer de un entorno virtual, con la
biblioteca pandas intalada, al que jupiter pueda acoplarse. Si jupiter no tiene
un entorno de trabajo predeterminado preparado con pandas, creamos uno nuevo 
ejecutando los sisguientes comandos:

```bash
python -m venv venv
source venv/bin/activate
pip install ipykernel
pip install pandas
pip install matplotlib 
python -m ipykernel install --user --name weather --display-name "weather-proyecto"
```

A demás de los instrumentos básicos habituales, necesitaremos también:

```bash
pip install jinja2 #Renderizar estilos en pandas
pip install grequests #Peticiones https asincronas
```
