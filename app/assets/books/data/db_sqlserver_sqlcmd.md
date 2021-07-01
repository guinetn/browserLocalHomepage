## sqlcmd

sqlcmd -S DESKTOP-5K4TURF\SQLEXPRESS -E
  –S  specify the SQL Server name of the instance
  -E  specify a trusted connection
  If no SQL Server name, it will try to connect to the local machine.

select DB_NAME()
GO
>>master
select name from sys.databases
go
SELECT SERVERPROPERTY('COLLATION')
GO
SELECT SERVERPROPERTY('EDITION')
GO
SELECT SERVERPROPERTY('IsIntegratedSecurityOnly')
GO
:ListVar

:SETVAR DATABASENAME "adventureworks2014"
USE $(DATABASENAME);
GO

select table_name from adventureworks2014.information_schema.tables
GO
select table_name, column_name from adventureworks2014.information_schema.columns
GO

CREATE DATABASE $(DATABASENAME);
GO 


columns.sql  (create this script file)
select * from adventureworks2014.information_schema.columns

invoke sqlcmd:
sqlcmd -S DESKTOP-5K4TURF\SQLEXPRESS -E -i c:\sql\columns.sql -o c:\sql\exit.txt
  -i is used to specify the input. You specify the script file with the queries.
  -o is used to show the results of the input in a file.
  exit.txt file will be created

backup.sql
BACKUP DATABASE [AdventureWorks2014] TO  DISK = N'C:\SQL\backup.bak'
sqlcmd -S DESKTOP-5K4TURF\SQLEXPRESS -E -i c:\sql\backup.sql -o c:\sql\output.txt



SQL Server & POWERSHELL

Microsoft SQL Server 2016 (SP1) (KB3182545) - 13.0.4001.0 (X64)
sqlcmd -S NGI5 -E
Server=localhost;Database=master;Trusted_Connection=True;
C:\Program Files\Microsoft SQL Server\130\Setup Bootstrap\Log\20170127_104750
C:\SQLServer2016Media\Developer

C:\Program Files\Microsoft SQL Server\130\SSEI\Resources
  Résumé de l'installation
  NOM D'INSTANCE                MSSQLSERVER
  ID D'INSTANCE                 MSSQLSERVER
  ADMINISTRATEURS SQL           NGI5\nguin
  FONCTIONNALITÉS INSTALLÉES    SQLENGINE
  VERSION                       13.0.4001.0, Service Pack 1

## SQL SERVER CLI

C:\Users\Bill> sqlcmd /?
Outil de ligne de commande Microsoft (R) SQL Server
Version 13.0.1601.5 NT
Copyright (c) 2015 Microsoft. Tous droits réservés.

utilisation : Sqlcmd            [-U ID de connexion]          [-P mot de passe]
  [-S serveur]            [-H nom d'hôte]          [-E connexion approuvée]
  [-N Chiffrer la connexion][-C Faire confiance au certificat du serveur]
  [-d utiliser le nom de base de données] [-l délai de connexion]     [-t délai de requête]
  [-h en-têtes]           [-s séparateur de colonnes]      [-w largeur d'écran]
  [-a taille du paquet]        [-e entrée d'écho]        [-I Activer les identificateurs marqués]
  [-c fin de commande]            [-L[c] répertorier les serveurs[nettoyer la sortie]]
  [-q « requête ligne de commande »]   [-Q « requête ligne de commande » et quitter]
  [-m niveau d'erreur]        [-V niveau de gravité]     [-W supprimer les espaces de fin]
  [-u sortie Unicode]    [-r[0|1] messages vers stderr]
  [-i fichier d'entrée]         [-o fichier de sortie]        [-z nouveau mot de passe]
  [-f <page de codes> | i:<page de codes>[,o:<page de codes>]] [-Z nouveau mot de passe et quitter]
  [-k[1|2] supprimer[replace] les caractères de contrôle]
  [-y largeur d'écran de longueur variable]
  [-Y largeur d'écran de longueur fixe]
  [-p[1] imprimer les statistiques[colon format]]
  [-R utiliser les paramètres régionaux du client]
  [-K intention de l'application]
  [-M basculement de plusieurs sous-réseaux]
  [-b Abandonner le lot d'instructions après erreur]
  [-v var = « valeur »...]  [-A Connexion admin dédiée]
  [-X[1] désactiver les commandes, le script de démarrage, les variables d'environnement [et quitter]]
  [-x désactiver la substitution de variable]
  [-j Imprimer les messages d'erreurs brutes]
  [-? afficher le résumé de la syntaxe]


Microsoft SQL Server 2016 (SP1) (KB3182545) - 13.0.4001.0 (X64)
run below commmand from command prompt
sqlcmd -S NGI5 -E

Server=localhost;Database=master;Trusted_Connection=True;
C:\Program Files\Microsoft SQL Server\130\Setup Bootstrap\Log\20170127_104750
C:\SQLServer2016Media\Developer
C:\Program Files\Microsoft SQL Server\130\SSEI\Resources

Select @@Version;
      → Microsoft SQL Server 2005 - 9.00.5000.00 (X64)   Dec 10 2010 10:38:40   Copyright (c) 1988-2005 Microsoft Corporation  Enterprise Edition (64-bit) on Windows NT 5.2 (Build 3790: Service Pack 2)
      → Microsoft SQL Server 2014 - 12.0.2000.8 (X64)   Feb 20 2014 20:04:26   Copyright (c) Microsoft Corporation  Express Edition (64-bit) on Windows NT 6.1 <X64> (Build 7601: Service Pack 1)
       8  →    SQL Server 2000
       9  →    SQL Server 2005
      10  →    SQL Server 2008
      11  →    SQL Server 2012
      12  →    SQL Server 2014

   
