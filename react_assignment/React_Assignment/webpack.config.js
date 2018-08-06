const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
module.exports={
	devtool:'inline-source-map',
	entry:'./client/client.js',
	output:{
		filename:'bundle.js'
	},
	devServer:{
		contentBase:'.',
		hot:true
	},
	plugins: [
		//new CleanWebpackPlugin(['dist']),
		//new HtmlWebpackPlugin({ title:"Hot Module Replacement"}),
   	 	new webpack.HotModuleReplacementPlugin(),
  	],
	module:{
		
		rules:[
			{
				test:/\.js$/,
				exclude:/node_modules/,
				loader:"babel-loader",
				options:{
					presets:["react","env","stage-1"]
				}
			}	
		]
	},
}
