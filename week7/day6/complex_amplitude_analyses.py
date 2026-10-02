import numpy as np


def complex_analyses(values):
    """
    a small numerical component that represents and analyses a set of complex amplitudes.
    If values is empty nd array it returns empty dictionary
    If it is not a valid 1D np array of complex number it raises TypeError exception.
    :param values: 1D NumPy array of complex amplitudes
    :return: dictionary of summary
    """
    # Initialize summary
    summary = {'magnitudes': np.empty(0, dtype=float),
               'normalised_vector': np.empty(0, dtype=complex),
               'probabilities': np.empty(0, dtype=complex)}

    if isinstance(values, np.ndarray) and np.isdtype(values.dtype, 'complex floating') and values.ndim == 1:
        if values.size > 0:
            # For non-empty vectors
            summary['magnitudes'] = np.abs(values)
            summary['normalised_vector'] = values
            if (norm := np.linalg.norm(values)) > 0:
                # Normalisation possible only for non zero vectors
                summary['normalised_vector'] = values/norm

            # calculating probabilities after finding the normalized vector
            summary['probabilities'] = np.abs(summary['normalised_vector'])**2
    else:
        raise TypeError
    return summary


def format_summary(summary):
    if len(summary) == 0:
        print("Empty vector provided. No summary available")
    else:
        print(f'Magnitude     : {summary["magnitudes"]}')
        print(f'Normal Vector : {summary["normalised_vector"]}')
        print(f'Probabilities : {summary["probabilities"]}')


def process_vectors(values = np.empty(0, dtype=complex)):
    summ = complex_analyses(values)
    format_summary(summ)


if __name__ == "__main__":
    process_vectors()
