#! /usr/bin/env python
"""本模块对数据进行清洗"""

import pandas as pd
import numpy as np
from loguru import logger



# 定义函数从Name里提取头衔
def getTitle(name):
    str1=name.split(',')[1] # Mr. Owen Harris
    str2=str1.split('.')[0]# Mr
#strip() 方法用于移除字符串头尾指定的字符（默认为空格）
    str3=str2.strip()
#直接用split会导致dataframe里的数据变成列表，接下去用字典匹配时会发生错误，这里用join将其重新变成字符串形式
    str4="".join(str3)
    return str4


def clean_data(train_data, val_data):


    #数据集
    
    full=pd.concat([train_data, val_data], ignore_index=True)
    logger.debug('数据集读取成功')
    logger.debug('tarin_data大小为：{}'.format(train_data.shape))
    logger.debug('val_data大小为：{}'.format(val_data.shape))
    logger.debug('full大小为：{}'.format(full.shape))
    
    
    
    # 填补空缺值
    full["Age"].fillna(full["Age"].median(),inplace=True) #年龄中位数填充
    full['Fare']=full['Fare'].fillna(full['Fare'].mean()) #票价均值填充
    full['Cabin'] = full['Cabin'].fillna( 'U' )#缺失数据比较多，Cabin(船舱号）缺失值填充为U，表示未知（Unknow） 
    full['Embarked']=full['Embarked'].fillna('S')
    
    # 性别处理
    full['Sex'] = full['Sex'].apply(lambda x: 1 if x == 'male' else 0)
    
    # 登船港口处理
    embarkedDf = pd.DataFrame()

    '''
    使用get_dummies进行one-hot编码，产生虚拟变量（dummy variables），列名前缀是Embarked
    '''
    embarkedDf = pd.get_dummies( full['Embarked'] , prefix='Embarked' )
    full = pd.concat([full,embarkedDf],axis=1)
    '''
    删除某列或某行数据可以用到pandas提供的方法drop
    axis为0时表示删除行，axis为1时表示删除列
    inplace代表操作是否对原数据生效，默认为False
    '''
    full.drop('Embarked',axis=1,inplace=True)
    
    # Pclass（客舱等级）
    #存放提取后的特征
    pclassDf = pd.DataFrame()

    '''
    使用get_dummies进行one-hot编码，产生虚拟变量（dummy variables），列名前缀是Pclass
    '''
    pclassDf = pd.get_dummies( full['Pclass'] , prefix='Pclass' )
    #添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full
    full = pd.concat([full,pclassDf],axis=1)
    # 因为已经对Pclass进行了进行了one-hot编码产生了它的虚拟变量（dummy variables），所以将Pclass（客舱等级）删除
    full.drop('Pclass',axis=1,inplace=True)
    
    # 乘客头衔提取
    
    titleDf=pd.DataFrame()
    #map函数：对Series每个数据应用自定义的函数计算
    titleDf['Title']=full['Name'].map(getTitle)
    title_mapDict = {
                    "Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                    "Dr":         "Officer",
                    "Rev":        "Officer",
                    "the Countess":"Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Mrs",
                    "Mlle":       "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mr",
                    "Mrs" :       "Mrs",
                    "Miss" :      "Miss",
                    "Master" :    "Master",
                    "Lady" :      "Royalty"
                    }

    #map函数：对Series每个数据应用自定义的函数计算
    titleDf['Title'] = titleDf['Title'].map(title_mapDict)

    #使用get_dummies进行one-hot编码
    titleDf = pd.get_dummies(titleDf['Title'])
    #添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full
    full = pd.concat([full,titleDf],axis=1)

    #删掉Name这一列
    full.drop('Name',axis=1,inplace=True)
    cabinDf = pd.DataFrame()
    # lambda 参数1，参数2：函数体或者表达式
    full[ 'Cabin' ] = full[ 'Cabin' ].map( lambda c : c[0] )
    ##使用get_dummies进行one-hot编码，列名前缀是Cabin
    cabinDf = pd.get_dummies( full['Cabin'] , prefix = 'Cabin' )
    #添加one-hot编码产生的虚拟变量（dummy variables）到泰坦尼克号数据集full
    full = pd.concat([full,cabinDf],axis=1)

    #删掉客舱号这一列
    full.drop('Cabin',axis=1,inplace=True)
    
    # 建立家庭人数和家庭类别
    #存放家庭信息
    familyDf = pd.DataFrame()
    '''
    家庭人数=同代直系亲属数（Parch）+不同代直系亲属数（SibSp）+乘客自己
    （因为乘客自己也是家庭成员的一个，所以这里加1）
    '''
    familyDf[ 'FamilySize' ] = full[ 'Parch' ] + full[ 'SibSp' ] + 1
    '''
    定义家庭类别
    1）小家庭Family_Single：家庭人数=1
    2）中等家庭Family_Small: 2<=家庭人数<=4
    3）大家庭Family_Large: 家庭人数>=5
    '''
    #if 条件为真的时候返回if前面内容，否则返回0
    familyDf[ 'Family_Single' ] = familyDf[ 'FamilySize' ].map( lambda s : 1 if s == 1 else 0 )
    familyDf[ 'Family_Small' ]  = familyDf[ 'FamilySize' ].map( lambda s : 1 if 2 <= s <= 4 else 0 )
    familyDf[ 'Family_Large' ]  = familyDf[ 'FamilySize' ].map( lambda s : 1 if 5 <= s else 0 )
    full = pd.concat([full,familyDf],axis=1)
    logger.debug('full.shape:{}'.format(full.shape))
    logger.debug('full.info:{}'.format(full.info()))
    
    #剔除无用的数据
    full.drop('Ticket',axis=1,inplace=True)
    full.drop('PassengerId',axis=1,inplace=True)
    full.drop('SibSp',axis=1,inplace=True)
    full.drop('Parch',axis=1,inplace=True)

    return full
