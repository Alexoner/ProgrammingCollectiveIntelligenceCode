function [y, sigma, p] = linInfer(X, model, t)
% Compute linear model reponse y = w'*x+b and likelihood
% X: n x d data
% t: n x 1 response

% w: weight
% b: bias
w = model.w;
b = model.b;
y = X*w'+b;

% nargout:within a function,return the number of values the caller expects
if nargout > 1
    % beta is called the precision: reciprocal of the variance
    beta = model.beta;

    % isfield(X,NAME):return true if X is a structure and includes an element
    % named NAME.
    if isfield(model,'V')   % V*V'=inv(S) 3.54
        % ???
        %X = model.V'*bsxfun(@minus,X,model.xbar);
        %sigma = sqrt(1/beta+dot(X,X,1));   % 3.59
        % by formula 3.59:sigma = sqrt(1/beta+X'*S*X)
        % and "inv(S)=alpha*I+beta+X'*X"
        sigma = sqrt(1/beta+X'*inv(V*V')*X)
    else
        sigma = sqrt(1/beta);
    end
    
    if nargin == 3 && nargout == 3
        % p = exp(logGaussPdf(t,y,sigma));
        p = exp(-0.5*(((t-y)./sigma).^2+log(2*pi))-log(sigma));
    end
end
        

