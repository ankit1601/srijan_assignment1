import React from 'react';
import ListSubheader from '@material-ui/core/ListSubheader';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import Collapse from '@material-ui/core/Collapse';
import ExpandLess from '@material-ui/icons/ExpandLess';
import ExpandMore from '@material-ui/icons/ExpandMore';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import StarBorder from '@material-ui/icons/StarBorder';

class ProcessDashboard extends React.Component{
        constructor(props){
                super(props);
                this.state = {open:true};
                this.state ={data:["RTD","Time-mizer","J-Fill Handheld","Wal-Mart Solution Center","Command Centre","Tim Hortons-3-button Dispenser","Sink-Mizer Plastic"]}
        }

        handleClick = ()=>{
                this.setState(state => ({open:!state.open}));
        }
        render(){
                console.log(this,"this");
                var that = this
                var menuList = this.state.data;
                var index=0
                return (
                        <List component="nav">
                         { menuList.map(function(menuitem){
                                index++;
                                return <div><ListItem button onClick={that.handleClick}>
                                                 <ListItemText key={index} inset primary={menuitem}/>
                                                        {that.state.open? <ChevronLeftIcon/> : <ChevronRightIcon/>}
                                                </ListItem>
                                                <Collapse in={that.state.open} timeout="auto" unmountOnExit>
                                                        <List component="div" disablePadding>
                                                                <ListItem button>
                                                                </ListItem>
                                                        </List>
                                                </Collapse>
                                        </div>

                        })}
                        </List>

                )


        }
}
export default ProcessDashboard

