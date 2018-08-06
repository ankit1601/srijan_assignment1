import React from 'react';
import {render} from 'react-dom';
import {BrowserRouter as Router} from 'react-router-dom';
import Button from '@material-ui/core/Button';
import App from './components/App.js'
/**function App(){
	return(
		<Button variant="contained" color="primary">
			Hello World
		</Button>
	);
}*/
render(<Router><App/></Router>,document.querySelector('#app'));
