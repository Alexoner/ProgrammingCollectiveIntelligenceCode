function [y, sigma, likelihood] = linInfer(X, model, t)
% Compute linear model reponse y = w'*x+b and likelihood
% X: n x d data
% t: n x 1 response

% w: d*1 weight vector,with w(0) as bias
w = model.w;
% actually,bias is supposed to be absorbed
b = model.b;
n = size(X,1);
X = [ones(n,1) X];
y = X*w;

% nargout:within a function,return the number of values the caller expects
if nargout > 1
    % beta is called the precision: reciprocal of the variance
    beta = model.beta;

    % isfield(X,NAME):return true if X is a structure and includes an element
    % named NAME.
    if isfield(model,'V')   % V*V'=S 3.54
        V = model.V;
        % ???
        %X = model.V'*bsxfun(@minus,X,model.xbar);
        X = X*model.V;
        % by equation (3.59):sigma = sqrt(1/beta+X'*S*X), and "inv(S)=alpha*I+beta+X'*X"
        %S = inv(V*V');
        %sigma = sqrt(1/beta+X*S*X'),but X here is a n-by-d design matrix,so convert
        % convert to product with the transpose to dot product
        sigma = sqrt(1/beta+dot(X,X,2));
    else
        sigma = sqrt(1/beta);
    end
    
    if nargin == 3 && nargout == 3
        likelihood = exp(logGaussPdf(t,y,sigma));
        %likelihood = exp(-0.5*(((t-y)./sigma).^2+log(2*pi))-log(sigma));
    end
end
