import os
import shutil

from_dir = '/caminho/para/sua/Downloads'
to_dir = '/caminho/para/sua/Arquivos_Documentos'

list_of_files = os.listdir(from_dir)

document_extensions = ['.txt', '.doc', '.docx', '.pdf']

for file_name in list_of_files:
 
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    
    if extension in document_extensions:
     
        path1 = from_dir + '/' + file_name
       
        path2 = to_dir + '/Arquivos_Documentos'
        
        path3 = to_dir + '/Arquivos_Documentos/' + file_name
      
        if os.path.exists(path2):
            
            print(f"Movendo {file_name} para {path3}")
           
            shutil.move(path1, path3)
        else:
           
            os.makedirs(path2)

            print(f"Movendo {file_name} para {path3}")
            
            shutil.move(path1, path3)
