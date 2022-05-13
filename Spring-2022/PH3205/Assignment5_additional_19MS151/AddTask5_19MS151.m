%----------------------------------------------------------------
  % Program : Find several lowest eigenmodes V(x) and
  % eigenenergies E of 1D Schrodinger equation
  %     -1/2*hbar^2/m(d2/dx2)V(x) + U(x)V(x) = EV(x)
  % for arbitrary potentials U(x).
  %----------------------------------------------------------------
  clc
  clear all
  % Parameters for solving problem in the interval -L < x < L.
  % PARAMETERS:
  L = 5;                   % Interval Length.
  N = 1001;%5;                % No of points.
  x = linspace(-L, L, N).';% Coordinate vector.
  dx = x(2) - x(1);        % Coordinate step.
  % POTENTIAL, choose one or make your own.
  
  % Finite square well of width 2w and depth given.
  w = L/50;
  %U = -500*(heaviside(x+w)-heaviside(x-w));
  % Two finite square wells of width 2w and distance 2a apart.
  %w = L/50;
  a = 3*w;
 U = -600*(heaviside(x+w-a) - heaviside(x-w-a)  + heaviside(x+w+a) - heaviside(x-w+a)  + heaviside(x+w-3*a) -heaviside(x-w-3*a) + heaviside(x+w+3*a) -heaviside(x-w+3*a))%+ x.^6 -0.5.*x.^3+sin(100.*x);
  
  % Three-point finite-difference representation of Laplacian
  % using sparse matrices, where you save memory by only
  % storing non-zero matrix elements.
  e = ones(N,1); % a column of ones
  Lap = spdiags([e -2*e e],[-1 0 1],N,N) / dx^2;
  % put -2e on the main diagonal and e-s on upper and lower diagonals
  % Total Hamiltonian.
  hbar = 1;
  m = 1;
  H = -1/2*(hbar^2/m)*Lap + spdiags(U,0,N,N); % 0 indicates main diagonal
  % put vector U on the main diagonal of NxN sparse matrix
  % Find lowest nmodes eigenvectors and eigenvalues of sparse matrix.
  nmodes = 3;
  [V,E] = eigs(H,nmodes,'smallestreal'); % find eigs.
  [E,ind] = sort(diag(E));            % convert E to vector and sort low to high.
  V = V(:,ind);                       % rearrange corresponding eigenvectors.
  % Generate plot of lowest energy eigenvectors V(x) and U(x).
  Usc = 10 * U * max(abs(V(:))) / max(abs(U));% rescale U for plotting.
  figure1 = figure;
  plot(x,V, x,Usc,'--k');                % plot V(x) and rescaled U(x).
  xlabel('x (m)');
  ylabel('Unnormalized wavefunction');
  % Add legend showing Energy of plotted V(x).
  legendLabels = [repmat('E = ',nmodes,1), num2str(E)];
  legend(legendLabels) % place lengend string on plot.
  ax = gca;
  ax.XLim = sqrt(2)*[-1 1];