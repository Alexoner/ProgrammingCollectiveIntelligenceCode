value=[50 40 30 50 30 24 36];
weight=[5 4 6 3 2 6 7];
TotalWeight=20;
beta=0:.01:1;
n=1000;


function X = Knapsack( value, weight, TotalWeight, beta, n )
% Input: value = array of values associated with object i.
% weight = array of weights associated with object i.
% TotalWeight = the total weight one can carry in the knapsack.
% beta = vector of beta values for simulated annealing.
% n = number of simulations per beta value.
% Output: FinalValue = maximum value of objects in the knapsack.
% FinalItems = list of objects carried in the knapsack.
% Entries in the vector correspond to object i
% being present in the knapsack.
v     = length(value);
W     = zeros(1,v);
Value = 0;
VW    = 0;
a     = length(beta);
nn    = n*ones(1,a);
for i = 1:a
    b = beta(i);
    for j=2:nn(i)
        m=0;
        while m==0
            c=ceil(rand*v);
            if W(c)==0
                m=1;
            end
        end
        TrialW=W;
        TrialW(c)=1;
        while sum(TrialW.*weight)>TotalWeight
            e=0;
            while e==0
                d=ceil(rand*v);
                if TrialW(d)==1
                    e=1;
                end
            end
            TrialW(d)=0;
        end
        f=sum(TrialW.*value)-sum(W.*value);
        g=min([1 exp(b*f)]);
        accept=(rand<=g);
        %Deterministic Model
        %if f>=0
        if accept
            W=TrialW;
            VW(j)=sum(W.*value);
        else
            VW(j)=VW(j-1);
        end
    end
    Value=[Value VW(2:length(VW))];
end
FinalValue=Value(length(Value))
x=0;
for k=1:length(W)
    if W(k)==1
        x=[x k];
    end
end
FinalItems=x(2:length(x))
end


Knapsack( value, weight, TotalWeight, beta, n)
