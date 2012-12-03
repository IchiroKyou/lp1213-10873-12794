<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Inscritos_2010_2011</class>
 <widget class="QMainWindow" name="Inscritos_2010_2011">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>633</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Análise de Inscritos no Ensino Superior</string>
  </property>
  <property name="windowIcon">
   <iconset>
    <normaloff>icon/estig.ico</normaloff>icon/estig.ico</iconset>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="bar2d_button">
    <property name="geometry">
     <rect>
      <x>130</x>
      <y>530</y>
      <width>106</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string>Barras 2D</string>
    </property>
   </widget>
   <widget class="QPushButton" name="bar3d_button">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>530</y>
      <width>106</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string>Barras 3D</string>
    </property>
   </widget>
   <widget class="QPushButton" name="line_h_button">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>530</y>
      <width>106</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string>Linhas H</string>
    </property>
   </widget>
   <widget class="QPushButton" name="line_m_button">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>530</y>
      <width>106</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string>Linhas M</string>
    </property>
   </widget>
   <widget class="QPushButton" name="line_hm_button">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>530</y>
      <width>106</width>
      <height>35</height>
     </rect>
    </property>
    <property name="text">
     <string>Linhas HM</string>
    </property>
   </widget>
   <widget class="QFrame" name="shell_frame">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>370</y>
      <width>781</width>
      <height>91</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
   </widget>
   <widget class="Line" name="line">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>470</y>
      <width>761</width>
      <height>20</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QLabel" name="escolha">
    <property name="geometry">
     <rect>
      <x>220</x>
      <y>490</y>
      <width>361</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Purisa'; font-size:11pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:12pt; font-weight:600; font-style:italic;&quot;&gt;Escolha o tipo de gráfico a visualizar:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QGraphicsView" name="graph_view">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>781</width>
      <height>351</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>33</height>
    </rect>
   </property>
   <widget class="QMenu" name="menuFicheiro">
    <property name="title">
     <string>File</string>
    </property>
    <addaction name="actionOpen"/>
    <addaction name="actionExport_as"/>
    <addaction name="actionQuit"/>
   </widget>
   <widget class="QMenu" name="menuHelp">
    <property name="title">
     <string>Help</string>
    </property>
    <addaction name="separator"/>
    <addaction name="actionAbout"/>
   </widget>
   <addaction name="menuFicheiro"/>
   <addaction name="menuHelp"/>
  </widget>
  <action name="actionCreditos">
   <property name="text">
    <string>Creditos</string>
   </property>
  </action>
  <action name="actionAbout">
   <property name="text">
    <string>About</string>
   </property>
  </action>
  <action name="actionOpen">
   <property name="text">
    <string>Open</string>
   </property>
  </action>
  <action name="actionExport_as">
   <property name="text">
    <string>Export As...</string>
   </property>
  </action>
  <action name="actionQuit">
   <property name="text">
    <string>Quit</string>
   </property>
  </action>
 </widget>
 <resources/>
 <connections/>
</ui>
