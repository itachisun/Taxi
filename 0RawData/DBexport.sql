USE [master]
GO

/****** Object:  Database [FCDBackup20100900_new]    Script Date: 11/1/2013 4:35:35 PM ******/
DROP DATABASE [FCDBackup20100900_new]
GO

/****** Object:  Database [FCDBackup20100900_new]    Script Date: 11/1/2013 4:35:35 PM ******/
CREATE DATABASE [FCDBackup20100900_new]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'sampledata', FILENAME = N'E:\taxi\FCDBackup20100900.mdf' , SIZE = 3438464KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
 LOG ON 
( NAME = N'samplelog', FILENAME = N'E:\taxi\FCDBackup20100900.ldf' , SIZE = 3456KB , MAXSIZE = UNLIMITED, FILEGROWTH = 10%)
GO

ALTER DATABASE [FCDBackup20100900_new] SET COMPATIBILITY_LEVEL = 90
GO

IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [FCDBackup20100900_new].[dbo].[sp_fulltext_database] @action = 'disable'
end
GO

ALTER DATABASE [FCDBackup20100900_new] SET ANSI_NULL_DEFAULT OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET ANSI_NULLS OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET ANSI_PADDING OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET ANSI_WARNINGS OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET ARITHABORT OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET AUTO_CLOSE ON 
GO

ALTER DATABASE [FCDBackup20100900_new] SET AUTO_CREATE_STATISTICS ON 
GO

ALTER DATABASE [FCDBackup20100900_new] SET AUTO_SHRINK OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET AUTO_UPDATE_STATISTICS ON 
GO

ALTER DATABASE [FCDBackup20100900_new] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET CURSOR_DEFAULT  GLOBAL 
GO

ALTER DATABASE [FCDBackup20100900_new] SET CONCAT_NULL_YIELDS_NULL OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET NUMERIC_ROUNDABORT OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET QUOTED_IDENTIFIER OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET RECURSIVE_TRIGGERS OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET  DISABLE_BROKER 
GO

ALTER DATABASE [FCDBackup20100900_new] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET TRUSTWORTHY OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET PARAMETERIZATION SIMPLE 
GO

ALTER DATABASE [FCDBackup20100900_new] SET READ_COMMITTED_SNAPSHOT OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET HONOR_BROKER_PRIORITY OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET RECOVERY FULL 
GO

ALTER DATABASE [FCDBackup20100900_new] SET  MULTI_USER 
GO

ALTER DATABASE [FCDBackup20100900_new] SET PAGE_VERIFY TORN_PAGE_DETECTION  
GO

ALTER DATABASE [FCDBackup20100900_new] SET DB_CHAINING OFF 
GO

ALTER DATABASE [FCDBackup20100900_new] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO

ALTER DATABASE [FCDBackup20100900_new] SET TARGET_RECOVERY_TIME = 0 SECONDS 
GO

ALTER DATABASE [FCDBackup20100900_new] SET  READ_WRITE 
GO

