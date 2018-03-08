/* nthperm.cpp
 * Ver 0.3
 * Peter H. Li 2013 FreeBSD License 
 *
 * See nthperm.m for documentation and a pure Matlab version of the same
 * algorithm.  As far as I am aware, the behavior of this Mex version is
 * identical to the pure Matlab version, but this version is about 10
 * times faster on my system.
 */
#include "mex.h"

// Function declarations
void t_nthperm(mxArray *outarr, unsigned long long n);


void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) {
  if (nrhs != 2)
    mexErrMsgIdAndTxt("nthperm:nrhs", "Arguments should be 1) a SORTED vector and 2) the desired permutation number (1-indexed).");
  
  if (!mxIsNumeric(prhs[0]))
    mexErrMsgIdAndTxt("nthperm:prhs", "First argument should be a SORTED numeric vector.");

  if (!mxIsNumeric(prhs[1]) || mxGetNumberOfDimensions(prhs[1]) != 2 || mxGetM(prhs[1]) != 1 || mxGetN(prhs[1]) != 1)
    mexErrMsgIdAndTxt("nthperm:prhs", "Second argument must be the positive scalar giving the permutation number desired (1-indexed).");

  // Convert Matlab 1-indexed to 0-indexed, check for nonnegative
  double n0 = mxGetScalar(prhs[1]) - 1;
  if (n0 < 0) mexErrMsgIdAndTxt("nthperm:prhs", "Second argument must be positive.");
  
  unsigned long long n = n0;
  plhs[0] = mxDuplicateArray(prhs[0]);
  t_nthperm(plhs[0], n);
}


/**
 * Circularly permute v at indices start through end,
 * i.e. 1 2 3 4 -> 4 1 2 3
 *
 * End is INCLUSIVE
 */
template <typename BidirectionalIterator>
void circshift(BidirectionalIterator start, BidirectionalIterator end) {
  mwIndex tmp = *end;
  for (; end > start; --end) *end = *(end-1);
  *start = tmp;
}

/**
 * Permute SORTED input array to the desired permutation.
 * Operates in place.
 */
template <typename RAIterator>
void nthperm(RAIterator start, const mwSize l, unsigned long long n) {
  mwIndex i;
  
  // Build factorial look-up table
  unsigned long long fact[l+1];
  fact[0] = 1;
  for (i = 1; i <= l; ++i) // Invariant: fact[i-1] is set
    fact[i] = fact[i-1] * i;
  
  // Initial wraparound in case n is greater than l!
  mwIndex d = n / fact[l];
  n -= d * fact[l];
  
  // Factorial radix rebasing
  for (i = 0; n > 0; ++i) {
    d = n / fact[l-i-1];
    n -= d * fact[l-i-1];
    
    // Permute v in-place to reflect factorial rebasing
    circshift(start+i, start+i+d);
  }

}


/**
 * Get data out in proper type and call low level function
 */
template <typename T>
void run_nthperm(mxArray *outarr, unsigned long long n) {
  const mwSize l = mxGetNumberOfElements(outarr);
  T* outdata = static_cast<T*>(mxGetData(outarr));
  nthperm(outdata, l, n); // Permutes outdata in-place
}


/**
 * Choose the template to call based on Matlab array numeric type
 */
void t_nthperm(mxArray *outarr, unsigned long long n) {
    
  switch (mxGetClassID(outarr)) {
    case mxDOUBLE_CLASS:
      run_nthperm<double>(outarr, n);
      break;

    case mxSINGLE_CLASS:
      run_nthperm<float>(outarr, n);
      break;

    case mxINT8_CLASS:
      run_nthperm<signed char>(outarr, n);
      break;

    case mxUINT8_CLASS:
      run_nthperm<unsigned char>(outarr, n);
      break;

    case mxINT16_CLASS:
      run_nthperm<signed short>(outarr, n);
      break;

    case mxUINT16_CLASS:
      run_nthperm<unsigned short>(outarr, n);
      break;

    case mxINT32_CLASS:
      run_nthperm<signed int>(outarr, n);
      break;

    case mxUINT32_CLASS:
      run_nthperm<unsigned int>(outarr, n);
      break;

    case mxINT64_CLASS:
      run_nthperm<signed long long>(outarr, n);
      break;

    case mxUINT64_CLASS:
      run_nthperm<unsigned long long>(outarr, n);
      break;

    default:
      mexErrMsgIdAndTxt("nthperm:prhs", "Unrecognized numeric array type.");
  }
  
}