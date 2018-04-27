

 console.log("Current Path => "+ __dirname);
  console.log(process.argv[2]+"content=>"+content);



**Command line input Read 

```
var readInput = readline.createInterface(process.stdin, process.stdout);


readInput.question('Please enter groupId ? ', (answer) => {
		  console.log('groupId => ', answer);
		  readInput.close();
		  });
		  
```