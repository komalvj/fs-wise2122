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
   - The 3 UML Diagrams that I choose for the TripPlanner project are: 
   - 1. Use Case Diagram: Describes the basic use case of my project.
   - 2. Activity Diagram: Describes the workflow of activity and interactions of a user
   - 3. Sequence Diagram: Extensive description of how and in what order the objects work in the application
  
3. DDD
   - TripPlanner uses Singleton and Factory design pattern.
     DataFactory.py loads the data from sample_places.py at the start of the program and stores it into data dictionary. Only single instance of the factory is          created and checked for while loading the objects. The dictionary of Places.py object, acts like a factory to fetch the places as required.
   - TestFastAPIProject is a RESTful service developed using FASTAPI(web app framework for developing RESTful APIs in Python).
     ![image](https://user-images.githubusercontent.com/92526578/154099461-f3aa5418-da38-44be-8f32-88c2535c3263.png)
     
     ![image](https://user-images.githubusercontent.com/92526578/154100927-5db9d305-d5f5-48b9-a126-c2c9afb765a5.png)

     
4. Metrics
   - Sonarcube -  Detect bugs, code smells, security hotspots and vulnerabilities in the source code
               -  Instead of setting up sonarqube locally, we used sonarcloud which connected to our project repository through just GitHub login.
               -  https://sonarcloud.io/project/overview?id=komalvj_fs-wise2122 : The initial scan of the project detected 2 code smells. After a minor code fix or                   removing unused method from the source code, this was reduced to one code smell. 
   
5. Clean Code Development
   - Line/Block comments are used wherever necessary. They explain the code better.
     ![image](https://user-images.githubusercontent.com/92526578/154102097-006989be-b05a-4cc0-b4a2-99ec43238faa.png)

   - All the variables are given relevant and self explanatory names. 
     ![image](https://user-images.githubusercontent.com/92526578/154102583-f1e91493-f3f1-4748-a740-59f2c8365ad6.png)

   - Functions are named appropiately as per what they do, the number of parameters passed are minimum or based on requirement.
   - Functions and variable names are not repeated.
   - Side effect free functions are used mostly to keep the application stateless.

6. Build Management
   As Python really does not need any Build Management tool, in order to understand a build management tool called Gradle, a small demo project called "gradle_demo"    was developed in Java. A simple Hello World program is built and ran using CLI.
   
   <img width="482" alt="image" src="https://user-images.githubusercontent.com/92526578/154012295-3b495f37-33ac-4723-a819-933c2a739072.png">
   <img width="482" alt="image" src="https://user-images.githubusercontent.com/92526578/154012306-09bb1d45-2b52-4e8b-ae94-67b0414632ed.png">

   
7. Unit-Tests
   An inbuilt test package is included in the application when creating the application. This is a basic assert statement confirming that the Hello World message is    printed without throwing any exceptions. 

8. Continuous Integration/Continuous Delivery
   GitHub Actions enables us to set up "CI" workflow for the repository. Any changes in the files, automatically triggers the workflow and new files are committed.
   Gradle is used to build the package, so that it is deployable. I tried setting up "Publish Java Package with Gradle" in order to publish the java packages to        GitHub packages.
   
9. IDE
   PyCharm CE was used as an IDE for development of the project.
   Keyboard shortcuts that I frequently used were: 
   1. Ctrl+R Runs the program, ⌘F2 Stops the program
   2. ⌘+/ Add or Remove line/block comment
   3. Debug: F8 Step over , F7 Step into
   4. Ctrl+Space Auto completes code
   5. ⌘+D Duplicates the line
   
10. DSL
    Groovy is a build script DSL used by gradle. Build script used by gradle(groovy based) for building the Java application "gradle_demo" 
      ![image](https://user-images.githubusercontent.com/92526578/154009907-de80020e-afed-4d1e-9fc3-8eaedbe137a0.png)
      
    UML can also be comsidered as a DSL used for modeling the application.

11. Functional Programming
    only final data structures
    
    ![image](https://user-images.githubusercontent.com/92526578/154105226-c2644a92-8e45-4eef-b601-a27c568413a5.png)

    (mostly) side effect free functions
    
    ![image](https://user-images.githubusercontent.com/92526578/154105534-9c687cae-a926-4f0c-8736-bae1ca111919.png)

    the use of higher-order functions
    
    ![image](https://user-images.githubusercontent.com/92526578/154108032-c56a5c23-dec2-4a4e-8e90-a7225c884b4e.png)
    
    functions as parameters and return values
    
    ![image](https://user-images.githubusercontent.com/92526578/154105642-c47d6450-50d7-4789-824e-486aff4725dc.png)

    use closures / anonymous functions
    
    ![image](https://user-images.githubusercontent.com/92526578/154104914-c8441958-e7b9-4e30-8dc2-c5f5eba21ce0.png)




