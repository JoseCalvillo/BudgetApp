import {PythonShell} from "python-shell";

PythonShell.run(
	'main.py',
	null,
	function(err){
		if(err) throw err;
		console.log("finished");

	}
);