<template>
    <div id=con2></div>
</template>

<script>
import axios from 'axios';
let echarts = require("echarts");
require("echarts/map/js/china.js");

var geoCoordMap = {
		'绵阳市': [104.679601,31.468644], 
		'广元市': [105.850418,32.443078],
		'重庆市': [106.558426,29.570489], 
		'南充市': [106.117502,30.845873], 
		'遂宁市': [105.599395,30.541201], 
		'广安市': [106.639525,30.463224], 
		'成都市': [104.081511,30.657303], 
		'内江市': [105.06458,29.587388], 
		"自贡市": [104.784417,29.347081], 
		"泸州市": [105.448516,28.879806], 
		"宜宾市": [104.649383,28.759518], 
		'毕节地区': [105.298571,27.291752], 
		'铜仁地区': [109.196426,27.739297], 
		
	};
	var CQData = [
		[{
			name: '绵阳市',
			value:176054
		}],
		[{
			name: '广元市',
			value: 144745
		}],
		[{
			name: '南充市',
			value: 603749
		}],

		[{
			name: '遂宁市',
			value: 362727
		}],
		[{
			name: '广安市',
			value: 1734606
		}],
		[{
			name: '成都市',
			value: 214604
		}],
		[{
			name: '内江市',
			value: 677662
		}],
		[{
			name: '自贡市',
			value: 177932
		}],
		[{
			name: '泸州市',
			value: 387675
		}],
		[{
			name: '宜宾市',
			value: 296239
		}],
		[{
			name: '毕节地区',
			value: 47986,
		}],
		[{
			name: '铜仁地区',
			value: 51622
		}],

	];
	var convertData = function(data) {
		var res = [];
		for(var i = 0; i < data.length; i++) {
			var dataItem = data[i];
			var fromCoord = geoCoordMap[dataItem[0].name];
			var toCoord = [106.558426,29.570489];
			if(fromCoord && toCoord) {
				res.push([{
					coord: fromCoord,
					value: dataItem[0].value
				}, {
					coord: toCoord,
				}]);
			}
		}
		return res;
	};

	var color = ['#a6c84c', '#ffa022', '#46bee9'];
	var series = [];
	[
		['重庆市', CQData]
	].forEach(function(item, i) {
		// console.log(item[1])
		series.push({
				type: 'lines',
				zlevel: 2,
				effect: {
					show: true,
					period: 1, //箭头指向速度，值越小速度越快
					trailLength: 0.32, //特效尾迹长度[0,1]值越大，尾迹越长重
					symbol: 'arrow', //箭头图标
					symbolSize: 5, //图标大小
				},
				lineStyle: {
					normal: {
						width: 1, //尾迹线条宽度
						opacity: 0, //尾迹线条透明度
						curveness: .3 //尾迹线条曲直度
					}
				},

				data: convertData(item[1])
			}, {
				type: 'effectScatter',
				coordinateSystem: 'geo',
				zlevel: 2,
				rippleEffect: { //涟漪特效
					period: 4, //动画时间，值越小速度越快
					brushType: 'stroke', //波纹绘制方式 stroke, fill
					scale: 4 //波纹圆环最大限制，值越大波纹越大
				},
				label: {
					normal: {
						show: true,
						position: 'right', //显示位置
						offset: [5, 0], //偏移设置
						formatter: function(params){//圆环显示文字
							return params.data.name;
						},
						fontSize: 13
					},
					emphasis: {
						show: true
					}
				},
				symbol: 'circle',
				symbolSize: function(val) {
					return 2 + val[2] / 100000; //圆环大小
				},
				itemStyle: {
					normal: {
						show: false,
						color: '#f00'
					}
				},
				data: item[1].map(function(dataItem) {
					return {
						name: dataItem[0].name,
						value: geoCoordMap[dataItem[0].name].concat([dataItem[0].value])
					};
				}),
			},
			//被攻击点
			{
				type: 'scatter',
				coordinateSystem: 'geo',
				zlevel: 2,
				rippleEffect: {
					period: 4,
					brushType: 'stroke',
					scale: 4
				},
				label: {
					normal: {
						show: true,
						position: 'right',
						//offset:[5, 0],
						color: '#00eaff',
						formatter: '{b}',
						textStyle: {
							color: "#00eaff"
						}
					},
					emphasis: {
						show: true
					}
				},
				symbol: 'pin',
				symbolSize: 20,
				itemStyle: {
					normal: {
						show: true,
						color: '#0ff'
					}
				},
				data: [{
					name: item[0],
					value: geoCoordMap[item[0]].concat([0]),
				}],
			}
		);
	});

let	option = {
        title: {
			text: '外来上网人员迁移图',
			left: 'center',
			textStyle: {
				color: "#F4F3EF"
				}
		},
		tooltip: {
			trigger: 'item',
			backgroundColor: 'rgba(166, 200, 76, 0.82)', //rgba(12, 204, 104, 0.92)
			borderColor: '#FFFFCC',
			showDelay: 0,
			hideDelay: 0,
			enterable: true,
			transitionDuration: 0,
			extraCssText: 'z-index:100',
			formatter: function(params, ticket, callback) {
				//根据业务自己拓展要显示的内容
				var res = "";
				var name = params.name;
				var value = params.value[params.seriesIndex + 1];
				res = "<span style='color:#fff;'>" + name + "</span><br/>数量：" + value;
				return res;
			}
		},
		backgroundColor:"#013954",
		visualMap: { //图例值控制
			min: 0,
			max: 1000000,
			calculable: false,
			show: true,
            color: ['#f44336', '#fc9700', '#ffde00', '#ffde00', '#00eaff'],
			textStyle: {
				color: '#fff'
			}
		},
		geo: {
			map: 'china',
			zoom: 7,
			label: {
				emphasis: {
					show: false
				}
			},
			roam: true, //是否允许缩放
			layoutCenter: [60.558426,-100.570489], //地图位置
			layoutSize: "100%",
			itemStyle: {
				normal: {
					color: 'rgba(101,109,117, .5)', //地图背景色
					borderColor: '#516a89', //省市边界线
					borderWidth: 1
				},
				emphasis: {
					color: 'rgba(71,85,102, .5)' //悬浮背景
				}
			}
		},
		series: series
	};

export default {
    data(){
        return {
            myChart:null,
        }
    },
    mounted(){
       this.myChart = echarts.init(document.getElementById('con2'));
	   this.myChart.setOption(option);
    }
}
</script>

<style>
    #con2{
    width: 345px;
	height: 300px
    }
</style>