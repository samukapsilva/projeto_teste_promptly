
### Explicação das Seções:

1. **PROJETO TESTE PROMPTLY**: 
   - O projeto teste promptly tem o objetivo de ingerir dados brutos de fontes distintas, transformar esses dados e gravar em um formato rico para servir a areas interessadas, criar data products, dashboards entre outros.
  
2. **Estrutura do Projeto**:
   - O projeto está estruturado em modulos independentes, incluindo as partes de **extração**, **transformação**, **carregamento** e **orquestração**.

3. **Requisitos e Instalação**:
   - Para instalar as dependências, execute o arquivo `requirements.txt`.
  
4. **Execução do Projeto**:
   - Para executar o projeto de forma manual, rode o aquivo main.py, para automarizar o processo, execute o arquivo promptly_orquestration.py, configurando os serviços necessários (PostgreSQL, MinIO, Airflow), que pode ser feito no arquivo config.properties.

5. **Estrutura de Diretórios**:
   - Os arquivos referentes a ingestão de dados, estão na pasta 'ingestion'
   - Os arquivos referentes à transformacao de dados, estao na pasta 'transformation'
   - O arquivo referente à orquestracao do projeto está na pasta orquestration
   - Uma base de conhecimento para ajudar em problemas comuns, está na pasta raíz do projeto com o onme knowledge_base.md

6. **Considerações Finais e TODO**:
   - Toda parte de log foi feita apenas na classe main, mas a ideia é expandir para o resto do projeto e depois trabalha-los com o elasticsearch, acompanhar no grafana etc.

7. **Licença**:
   - Criado apenas para exercicio e cedido à promptly sem nenhuma exigencia de direito autoral.