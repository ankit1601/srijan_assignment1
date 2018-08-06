import React from 'react';
import PropTypes from 'prop-types';
import {withStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ProcessDashboard from './processdashboard/ProcessDashboard';


const styles = {
	root:{
		flexGrow:1,
	},
	flex:{
		flex:1,
	},
	menuButton:{	
		marginLeft: -12,
		marginLeft: 20,
	}
		
}

class App extends React.Component{
	constructor(props){
		super(props);
	}
	render(){
		return(
		<div>
			<div className = {styles.root}>
				<AppBar position="static">
					<Toolbar>
						<IconButton color="inherit" aria-label="Menu">
							<MenuIcon />
						</IconButton>
						<Typography variant="title" color="inherit">
                                                        Product List
                                                </Typography>
					</Toolbar>
				</AppBar>
			</div>
			<ProcessDashboard/>
		</div>
		)
	}
}	
App.propTypes = {
	classes: PropTypes.object.isRequired	
};
export default withStyles(styles)(App);




