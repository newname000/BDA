#First google collab
#Runtime -> Change Runtime type ->  R

install.packages("igraph")

# Load igraph library
library(igraph)

# Create an undirected graph
g <- graph(c(1, 2, 2, 3, 3, 4, 4, 1), directed = FALSE, n = 7)

# Plot the graph
plot(g, vertex.color = "green", vertex.size = 40, edge.color = "red")

# Create a directed graph with names
g1 <- graph(c("Asmit", "Raghu", "Priyanka", "Pooja", "Pooja", "Asmit", "Asmit", "Karan", "Pooja"), directed = TRUE)

# Network measures
degree_all <- degree(g1, mode = 'all')
degree_in <- degree(g1, mode = 'in')
degree_out <- degree(g1, mode = 'out')
diameter_value <- diameter(g1, directed = FALSE, weights = NA)
edge_density_value <- edge_density(g1, loops = FALSE)
reciprocity_value <- reciprocity(g1)
closeness_value <- closeness(g1, mode = 'all', weights = NA)
betweenness_value <- betweenness(g1, directed = TRUE, weights = NA)
edge_betweenness_value <- edge_betweenness(g1, directed = TRUE, weights = NA)

# Read data file
data <- read.csv('https://raw.githubusercontent.com/bkrai/R-files-from-YouTube/main/networkdata.csv', header = TRUE)

# Prepare the data for graph creation
y <- data.frame(from = data$first, to = data$second)

# Create a network from the data
net <- graph.data.frame(y, directed = TRUE)

# Set vertex labels and calculate degree
V(net)$label <- V(net)$name
V(net)$degree <- degree(net)

# Histogram of node degrees
hist(V(net)$degree)

# Network diagram
plot(net)

# Highlighting degrees & layouts
plot(net, vertex.color = rainbow(52), vertex.size = V(net)$degree * 0.4, edge.arrow.size = 0.1, layout = layout.fruchterman.reingold)

# Hubs and authorities
hub_score <- hub_score(net)$vector
authority_score <- authority.score(net)$vector

par(mfrow = c(1, 2))
set.seed(222)

# Plot Hubs
plot(net, vertex.size = hub_score * 30, main = 'Hubs', vertex.color = rainbow(52), edge.arrow.size = 0.1, layout = layout.kamada.kawai)

# Plot Authorities
plot(net, vertex.size = authority_score * 30, main = 'Authorities', vertex.color = rainbow(52), edge.arrow.size = 0.1, layout = layout.kamada.kawai)

par(mfrow = c(1, 1))

# Community detection
net <- graph.data.frame(y, directed = FALSE)
cnet <- cluster_edge_betweenness(net)

# Plot community detection results
plot(cnet, net)
