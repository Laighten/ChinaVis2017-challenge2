<template>
    <div id="con">
	</div>
</template>

<script>
import axios from 'axios';
let echarts = require("echarts");
require("echarts/extension/bmap/bmap");
import _ from "lodash";


let option = {
	//backgroundColor: '#404a59',
	title: {
		text: '违法网吧分布',
		left: '40%'
		},
	tooltip: {
		trigger: 'item'
		},
	bmap: {
		center: [107.0000, 29.87555],
		zoom: 11,
		roam: true,
		mapStyle: {
			
			styleJson:[{
					"featureType": "background",
					"elementType": "geometry",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "land",
					"elementType": "geometry",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "highwaysign",
					"elementType": "labels.text.stroke",
					"stylers": {
						"weight": 2.4
					}
				}, {
					"featureType": "nationalway",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "nationalway",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "provincialway",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "provincialway",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "cityhighway",
					"elementType": "labels",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "cityhighway",
					"elementType": "geometry",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "arterial",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "arterial",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "tertiaryway",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "tertiaryway",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "water",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "water",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "green",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "building",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "manmade",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "manmade",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "subwaystation",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "education",
					"elementType": "labels.text",
					"stylers": {
						"fontsize": 35
					}
				}, {
					"featureType": "education",
					"elementType": "labels.text.fill",
					"stylers": {
						"weight": 90
					}
				}, {
					"featureType": "education",
					"elementType": "geometry",
					"stylers": {
						"color": "#d0021bff"
					}
				}, {
					"featureType": "medical",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "medical",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "scenicspots",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "scenicspots",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "entertainment",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "estate",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "transportation",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "transportation",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "shopping",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "road",
					"elementType": "geometry",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "road",
					"elementType": "labels",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "airportlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "airportlabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "scenicspotslabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "scenicspotslabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "medicallabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "medicallabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "entertainmentlabel",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#ffffffff"
					}
				}, {
					"featureType": "estatelabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "estatelabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "businesstowerlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "businesstowerlabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "companylabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "companylabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "governmentlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "governmentlabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "restaurantlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "restaurantlabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "hotellabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "hotellabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "shoppinglabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "shoppinglabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "lifeservicelabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "lifeservicelabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "carservicelabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "carservicelabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "transportationlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "transportationlabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "financelabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "financelabel",
					"elementType": "labels.icon",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "continent",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "country",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "city",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#4a4a4aff"
					}
				}, {
					"featureType": "district",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#4a4a4aff"
					}
				}, {
					"featureType": "town",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#4a4a4aff"
					}
				}, {
					"featureType": "village",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#4a4a4aff"
					}
				}, {
					"featureType": "highway",
					"elementType": "geometry",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "highway",
					"elementType": "labels",
					"stylers": {
						"visibility": "off"
					}
				}, {
					"featureType": "educationlabel",
					"elementType": "labels.text.stroke",
					"stylers": {
						"weight": 1
					}
				}, {
					"featureType": "educationlabel",
					"elementType": "labels.text",
					"stylers": {
						"fontsize": 30
					}
				}, {
					"featureType": "educationlabel",
					"elementType": "labels",
					"stylers": {
						"visibility": "on"
					}
				}, {
					"featureType": "educationlabel",
					"elementType": "labels.text.fill",
					"stylers": {
						"color": "#d0021bff",
						"weight": 10
					}
				}]
								// style:"dark",
			}
		},
		series: [
				{
					id:"data1",
					name: 'illgbar',
					type: 'scatter',
					coordinateSystem: 'bmap',
					//data1:[],
					// symbolSize: function (val) {
					// 		return val[1] / 6;
					// 	},
					tooltip: {
						show: true,
						formatter: '{b}'
					},
					label: {
						normal: {
							formatter: '{b}',
							position: 'right',
							show: false
						},
						emphasis: {
							show: true
						}
					},
					itemStyle: {
						normal: {
							color: 'blue'
						}
					},
					symbolSize:6,
				},
				{
					id:"data2",
					name: 'Innetbar',
					type: 'scatter',
					coordinateSystem: 'bmap',
					//data2:[],
					// symbolSize: function (val) {
					// 		return val[1] / 6;
					// 	},
					tooltip: {
						show: true,
						formatter: '{b}'
					},
					label: {
						normal: {
							formatter: '{b}',
							position: 'right',
							show: false
						},
						emphasis: {
							show: true
						}
					},
					itemStyle: {
						normal: {
							color: 'red'
						}
					},
					symbolSize:6,
				}
			]
};



export default {
    data() {	
		return{
			myChart: null,
			ldata:[],
			Mdata:[],
			peakData: []
			
		}
	},
	methods:{
		    
			getScatterData: function() {
					const _this = this;
					return [new Promise(function(resolve, reject) {
						axios
							.get("/data/api/JuvBlue")
							.then(response => {
							let data = response.data;
							data = data.map(obj => {
								let arr = _.values(obj);
								let siteid = arr.shift();
								arr.push(siteid);
								return arr;
							});
							//单个series的data的临界值是2999，超过后渲染会卡顿，因此设置每2000个点为一个series
							_this.ldata = data;
							resolve();
							})
							.catch(error => {
							reject(error);
							});
						
					}),
				
				new Promise(function(resolve, reject){
					axios
							.get("/data/api/JuvRed")
							.then(response=>{
								let data = response.data;
								data = data.map(obj =>{
									let arr= _.values(obj);
									let siteid = arr.shift();
									arr.push(siteid);
									return arr;
								});
								_this.Mdata = data;
								resolve();
							})
							.catch(error => {
								reject(error);
							})
				})]
			
			},
			listenMap() {
				this.myChart.on('click', params => {
					//console.log(params)
					let netId = params.value[3]
					this.getNetbarpeople(netId).then(()=> {
						//console.log(this.peakData)
						this.$root.Bus.$emit('peakData', this.peakData)
						this.$root.Bus.$emit('lightOFF', true)
					})
				})
			},
			getNetbarpeople(netId) {
				const _this = this
				return new Promise((resolve,reject) => {
					axios({
						method: 'post',
						url: '/data/api/ClickTime',
						data: [[netId]]
					}).then((response) => {
						_this.peakData  = response.data
						
						resolve()
					}).catch((error) => {
						console.log(error)
						reject()
					})
				})
			}	
	},	
	mounted() {
		this.myChart = echarts.init(document.getElementById('con'));
		this.myChart.setOption(option);
		console.log(this.myChart.getOption())
		//this.laodAllUser()
		
		const _this=this;
		this.getScatterData()[0].then(() => {
		
           _this.myChart.setOption({
				series: [{
					id:"data1",
					data: _this.ldata
				}]
			})
		});
		this.getScatterData()[1].then(() => {
	
           _this.myChart.setOption({
				series: [
				{
				    id:"data2",
					data: _this.Mdata
				}]
			})
		});
		
		/* this.getScatterData().then(() => {
		console.log(_this.ldata);
		console.log(_this.Mdata);
           _this.myChart.setOption({
				series: [{
					id:"data1",
					data: _this.ldata
				},
				{
				    id:"data2",
					data: _this.Mdata
				}]
			})
		}); */
		this.listenMap();

		var bmap = this.myChart.getModel().getComponent('bmap').getBMap();
		bmap.addControl(new BMap.MapTypeControl());
		

		var local = new BMap.LocalSearch(bmap,{
				renderOptions:{map: bmap}
			});
		local.search("小学");
		//local.search("中学")
		//local.searchInBounds("小学", bmap.getBounds());

	},
	created(){
		
	}
	
}
</script>

<style>

#con {	
	height: 580px;

}
</style>