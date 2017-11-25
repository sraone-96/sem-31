function [ J, cluster_centers, idx ] = run_KMeans( X, initial_clusters_centers, max_iters )

[m, ~] = size(X);
K = size(initial_clusters_centers, 1);
cluster_centers = initial_clusters_centers;
previous_cluster_centers = cluster_centers;
idx = zeros(m, 1);

for i=1:max_iters
    % For each example in X, assign it to the closest centroid
    idx = findClosestClusters( X, cluster_centers );
    
    % Optionally, plot progress here
   %{
    if plot_progress
        plotProgresskMeans(X, cluster_centers, previous_cluster_centers, idx, K, i);
        previous_cluster_centers = cluster_centers;
        %fprintf('Press enter to continue.\n');
        %pause;
    end
    %}
    % Given the memberships, compute new centroids
    cluster_centers = compute_cluster_centers( X, idx, K );
end
J = 0;
for i = 1 : size(X,1)
    J = J + sqrt(sum((X(i,:) - cluster_centers(idx(i),:)).^2));
end
%if plot_progress
    %hold off;
    

end

function [ cluster_centers ] = compute_cluster_centers( X, idx, K )
[m, n] = size(X);
cluster_centers = zeros(K, n);
number_of_samples=zeros(K,1);
for i=1:m
    number_of_samples(idx(i))=number_of_samples(idx(i))+1;
    cluster_centers(idx(i),:)=(cluster_centers(idx(i),:) + X(i,:));
end
cluster_centers=bsxfun(@rdivide,cluster_centers,number_of_samples);
end

function [ idx ] = findClosestClusters( X, cluster_centers )
K = size(cluster_centers,1); 
idx = zeros(size(X,1), 1);
distances=zeros(K,1);
for i=1:size(X,1)
    for k=1:K
        distances(k)=sum((X(i,:)-cluster_centers(k,:)).^2);
    end
    [~,idx(i)]=min(distances);
end
end
