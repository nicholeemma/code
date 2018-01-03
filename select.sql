select * from business_trip_data;
INSERT INTO exceltomysql (gender,name) VALUES ('女','佳玥');
load data local infile 'F:/test.txt' into table exceltomysql character set utf8 fields terminated by '\t';
load data local infile 'F:/business_trip_data.txt' into table business_trip_data character set utf8 fields terminated by '\t';
create table business_trip_data(流水号 varchar(100),用车人 varchar(100),部门 varchar(50),成本中心 varchar(100),城市 varchar(50),起点 varchar(500),终点 varchar(500), 订单时间 varchar(500), 开始时间 varchar(500),里程 float, 行驶时间 varchar(200), 订单金额 float, 实际金额 float,用车来源 varchar(50), 支付途径 varchar(50), 审批人 varchar(100), 审批状态 varchar(50)
);
DELETE FROM business_trip_data WHERE 流水号 = '流水号';

SELECT * FROM business_trip_data
WHERE 起点 LIKE '%站%' or 终点 NOT LIKE '%站%' or 起点 NOT LIKE '%站' or 终点 NOT LIKE '%站' ;

SELECT * FROM business_trip_data
WHERE 起点 not like '%站' and 终点 not like '%站' and 终点 not like '%机场%' and 终点 not like '%站%' and 起点 not like '%机场%' and 起点 not like '%站%' and 起点 not like '张江集电港%' and 起点 not like '美敦力' and 终点 not like '张江集电港%' and 终点 not like '美敦力';