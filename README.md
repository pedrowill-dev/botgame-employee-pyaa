# Botgame Employee Data Migration


Este projeto foi desenvolvido utilizando as bibliotecas `pywinauto` e `selenium` para automatizar a migração de dados de funcionários.


<h1> Descrição do projeto</h1>

O objetivo deste projeto é automatizar o processo de migração de dados de funcionários por meio da interação com o site `EmployeeDataMigration` e do aplicativo EmployeeList.exe.


<h2> 1. Acesso ao site - EmployeeDataMigration</h2>

Nesta parte do projeto, o programa automatiza o acesso ao site `EmployeeDataMigration` e interage com o formulário para fornecer o <b>ID</b> do funcionário e submeter os dados. A seguir estão os detalhes de como essa interação é realizada<br>


![image](https://github.com/pedrowill-dev/botgame-employee-pyaa/assets/110316192/e4aaa268-6e8a-4656-9b03-b434b02240c9)


<h2>2. Acesso ao desktop - EmployeeList</h2>
<p></p>Consulta das informações no aplicativo EmployeeList.exe: O programa abrirá o aplicativo e realizará a consulta das informações do funcionário com base no ID fornecido.</p>

![image](https://github.com/pedrowill-dev/botgame-employee-pyaa/assets/110316192/472e94b3-f909-4ca4-9f65-4dc786fe4006)

<hr>

<h2>Requisitos</h2>

Certifique-se de ter os seguintes requisitos instalados em seu ambiente de desenvolvimento:

- Python 3.x
- Biblioteca pyautowin
- Biblioteca selenium
- WebDriver para o navegador utilizado (por exemplo, ChromeDriver)


<h2> Instalação </h2>
<p></p>Siga as etapas abaixo para configurar o ambiente de desenvolvimento:</p>

1. Clone o repositório do projeto:
   
````bash
git clone https://github.com/pedrowill-dev/botgame-employee-pyaa.git
````

2. Download de todas as libs do projeto:

````bash
pip install -r requirements.txt
````

3. Execução do projeto

````bash
python run.py
````



