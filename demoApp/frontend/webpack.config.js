var path = require('path');
var webpack = require('webpack');

module.exports = {
	entry: {
		index: './src/app/main.js',
		upload: './src/app/upload.js',
		profile: './src/app/profile.js',
		users: './src/app/users.js',
	},
	output: {
		path: path.resolve(__dirname, "static", "frontend"),
		filename: "[name].js"
	},
	resolve: {
		extensions: ['.js', '.jsx']
	},
	plugins: [
		// automatically load modules instead of having to import or require them everywhere
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery'
		}),
	],
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader"
				}
			},
			{
				test: /\.css$/,
				exclude: /node_modules/,
				use: ['style-loader', 'css-loader', 'sass-loader',],
			},
			{
				test: /\.css$/,
				include: /node_modules/,
				loaders: ['style-loader', 'css-loader'],
			},
			{
				test: /\.(pdf|jpg|png|gif|svg|ico)$/,
				use: [
					{
						loader: 'url-loader'
					},
				]
			},
			{
				test: /\.svg$/,
				loader: 'svg-inline-loader'
			}
		]
	}
};

