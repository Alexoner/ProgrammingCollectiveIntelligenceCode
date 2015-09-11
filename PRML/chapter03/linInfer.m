function [y, sigma, p] = linInfer(X, model, t)
% Compute linear model reponse y = w'*x+b and likelihood
% X: d x n data
% model.w: weight vector
% model.b: bias
% t: 1 x n response
% y: 1 * n prediction
% sigma:square root of variance(standard deviation)
% p: likelihood function
w = model.w;
b = model.b;
y = w'*X+b;
if nargout > 1
    % beta: Gaussian precision
    beta = model.beta;

    if isfield(model,'V')   % V*V'=inv(S) 3.54
        X = model.V'*bsxfun(@minus,X,model.xbar);
        sigma = sqrt(1/beta+dot(X,X,1));   % 3.59
    else
        sigma = sqrt(1/beta);
    end
    
    if nargin == 3 && nargout == 3
%         p = exp(logGaussPdf(t,y,sigma));
        p = exp(-0.5*(((t-y)./sigma).^2+log(2*pi))-log(sigma));
    end
end
