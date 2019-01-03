-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	6.0.7-alpha-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema stp_python
--

CREATE DATABASE IF NOT EXISTS stp_python;
USE stp_python;

--
-- Definition of table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE `books` (
  `bid` int(11) NOT NULL,
  `title` varchar(30) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `author` varchar(20) DEFAULT NULL,
  `quant_avail` int(11) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `books`
--

/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` (`bid`,`title`,`subject`,`author`,`quant_avail`) VALUES 
 (101,'Learning java','java','James Gosling',20),
 (102,'Let Us C','C Language','Yashwant Kanetkar',18);
/*!40000 ALTER TABLE `books` ENABLE KEYS */;


--
-- Definition of table `emp_detail`
--

DROP TABLE IF EXISTS `emp_detail`;
CREATE TABLE `emp_detail` (
  `empid` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  `doj` date DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  PRIMARY KEY (`empid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `emp_detail`
--

/*!40000 ALTER TABLE `emp_detail` DISABLE KEYS */;
INSERT INTO `emp_detail` (`empid`,`name`,`dept`,`doj`,`salary`) VALUES 
 (900001,'Ayaz','CSE','2018-01-01',20000),
 (900002,'Zaved','CSE','2018-02-01',25000),
 (900003,'Shivangi','CSE','1995-04-01',15000),
 (900004,'Samiksha','CSE','2017-01-01',20000);
/*!40000 ALTER TABLE `emp_detail` ENABLE KEYS */;


--
-- Definition of table `issue_detail`
--

DROP TABLE IF EXISTS `issue_detail`;
CREATE TABLE `issue_detail` (
  `bid` int(11) DEFAULT NULL,
  `issueto` int(11) DEFAULT NULL,
  `issueby` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `issue_detail`
--

/*!40000 ALTER TABLE `issue_detail` DISABLE KEYS */;
INSERT INTO `issue_detail` (`bid`,`issueto`,`issueby`) VALUES 
 (102,100003,900001),
 (102,100003,900002);
/*!40000 ALTER TABLE `issue_detail` ENABLE KEYS */;


--
-- Definition of table `login`
--

DROP TABLE IF EXISTS `login`;
CREATE TABLE `login` (
  `lid` int(11) NOT NULL,
  `pass` varchar(20) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `role` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

/*!40000 ALTER TABLE `login` DISABLE KEYS */;
INSERT INTO `login` (`lid`,`pass`,`name`,`role`) VALUES 
 (100001,'pass1','Zaved','stu'),
 (100002,'pass2','Ayaz','stu'),
 (100003,'pass3','Shivangi','stu'),
 (100004,'pass4','Samiksha','stu'),
 (900001,'passad1','Ayaz','emp'),
 (900002,'passad2','Zaved','emp'),
 (900003,'passad3','Shivangi','emp'),
 (900004,'passad4','Samiksha','emp');
/*!40000 ALTER TABLE `login` ENABLE KEYS */;


--
-- Definition of table `stu_detail`
--

DROP TABLE IF EXISTS `stu_detail`;
CREATE TABLE `stu_detail` (
  `rollno` int(11) NOT NULL,
  `name` varchar(30) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  `sem` varchar(10) DEFAULT NULL,
  `batch` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`rollno`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `stu_detail`
--

/*!40000 ALTER TABLE `stu_detail` DISABLE KEYS */;
INSERT INTO `stu_detail` (`rollno`,`name`,`dept`,`sem`,`batch`) VALUES 
 (100001,'Zaved','CSE','5','D'),
 (100002,'Ayaz','CSE','5','F'),
 (100003,'Shivangi','CSE','5','F'),
 (100004,'Samiksha','CSE','5','F');
/*!40000 ALTER TABLE `stu_detail` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
