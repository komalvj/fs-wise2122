# fs-wise2122
Fortgeschrittene Softwaretechnik (WiSe2122) Exercise

1. Git is a version control and source code management system used to track changes in the set of files used in a particular project. For the purpose of my project I have used the internet hosted version of Git, i.e. GitHub. With GitHub, you can directly update the uploaded files in the editor online and commit the changes.
The following steps were followed in creation of the repository "fs-wise2122":
   - Created a public repository with name "fs-wise2122", branch name as "main".
   - Drag and dropped my entire project "TripPlanner" on the console. 
     This is similar to Git command: 
     $ git add
   - The uploaded files can be committed using "Commit Changes" button. Description can be added to specify the changes made. There is an option to update in the 
     main branch or create a new branch. 
     This is similar to Git command:
     $ git commit -m "small discription"
     $ git push
   - Once the files are successfully uploaded, the said respository is available to public for pull requests (Also available at a click of a button in GitHub. Git        command: 
     $ git pull
     
2. UML Diagram
   - https://github.com/komalvj/fs-wise2122/tree/main/UML%20Diagrams
  
3. DDD
   - TripPlanner uses Singleton design pattern.
     DataFactory.py loads the data from sample_places.py at the start of the program and stores it into data dictionary. Only single instance of the factory is          created and checked for while loading the objects.
     
4. Metrics
   - Sonarcube -  Detect bugs, code smells, security hotspots and vulnerabilities in the source code
               -  https://sonarcloud.io/project/overview?id=komalvj_fs-wise2122
   
5. Clean Code Development



