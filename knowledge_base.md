########################################################################################################################
venv\Scripts\activate
venv\Scripts\activate : File C:\Users\samukapsilva\projeto_teste_promptly\venv\Scripts\Activate.ps1 cannot be loaded because running scripts is 
disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ venv\Scripts\activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess


Solution: 

Abra o PowerShell como administrador:

Pressione Win + S, digite PowerShell, clique com o botão direito e selecione Executar como Administrador.
Verifique a política de execução atual:

Get-ExecutionPolicy

Se o retorno for Restricted, significa que scripts não podem ser executados.

Alterar a política de execução
No PowerShell aberto como administrador, altere a política para permitir execução de scripts locais:

powershell

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

RemoteSigned: Permite execução de scripts locais sem assinatura. Scripts baixados precisam ser assinados.


OBS:
Caso queira voltar à configuração anterior pode executar:

Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Restricted
########################################################################################################################
