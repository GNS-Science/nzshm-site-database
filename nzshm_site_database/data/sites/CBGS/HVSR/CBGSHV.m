% Liam Wotherspoon
% Figures for H/V Spectral ratio measurements ChCh SMS

% M-file for creation of plots
% Import the test data from saved txt file.

%---------------------------------
%Data
HVInput = dlmread('CBGSDeep.hv','\t',7,0);

% Create a matrix for the each column
Freq = HVInput(:,1);

Lower = HVInput(:,3);

Mean = HVInput(:,2);

Upper = HVInput(:,4);

axismaxY = 6;
axisminY = 0;
 
axismaxX = 10;
axisminX = 0.1;

%
%
%Create a comboplot of the two together
 
figure('Position',[0 0 (400) (400)]);

%hl1=line(SPTType,Depth1,'Color','k','LineWidth',1.5);
hl2=line(Freq,Mean,'Color','r','LineStyle','-','LineWidth',2);

hl2=line(Freq,Lower,'Color','r','LineStyle','--','LineWidth',2);

hl2=line(Freq,Upper,'Color','r','LineStyle','--','LineWidth',2);

peak1 = 0.155;


%hl1=line([peak1;peak1],[0;axismaxY],'Color',[0.5 0.5 0.5],'LineWidth',2,'LineStyle','-');
%hl1=line([4;4.5],[-9.2;-9.2],'Color','k','LineWidth',1,'LineStyle','-');
%hl1=line([4;4.5],[-21.3;-21.3],'Color','k','LineWidth',1,'LineStyle','-')

ax1=gca;
set(ax1,'TickDir','in','XLim',[axisminX axismaxX],'XScale','log','XMinorTick','off','YLim',[axisminY axismaxY],'FontSize',7,'FontName', 'Helvetica','XTick',[0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10],'XTickLabel',{'','','','','0.1','0.2','0.3','','0.5','','','','','1','2','3','4','5','','','','','10'});
%set(ax1,'TickDir','in','XLim',[axisminX axismaxX],'XScale','log','XMinorTick','off','YLim',[axisminY axismaxY],'FontSize',7,'FontName', 'Helvetica','XTickLabel',{'0.1' '1' '10'});

title('','FontSize',12);
h = legend('Mean','Mean \pm 1SD',2);

legendshrink(0.6,'right',h);
set(h,'PlotBoxAspectRatioMode','manual');
set(h,'PlotBoxAspectRatio',[1 1.5 1]);
set(h,'DataAspectRatioMode','manual');
set(h,'DataAspectRatio',[0.55 1.3 1]);
Pos = get(h,'Position');
PosNew = Pos(1);
Pos(3) = (Pos(3)-Pos(1))*0.8+Pos(1);
Pos(1) = 0.675;
set(h,'Position',Pos);


xlabel('Frequency (Hz)','FontSize',8,'FontName','Helvetica');
ylabel('H/V Spectral Ratio','FontSize',8,'FontName','Helvetica');
 

ax2=axes('Position',get(ax1,'Position'),'YAxisLocation','right','XAxisLocation','top','TickDir','in','Color','none','YLim',[axisminY axismaxY],'YTick',[],'XTick',[]); 




