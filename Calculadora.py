{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "Calculadora.ipynb",
      "authorship_tag": "ABX9TyOh/5xAxEoXH5eWoPL7VBef",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Alevivaldi/Python/blob/main/Calculadora.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KwvBRRwBmaEZ",
        "outputId": "8f85d457-8044-44d8-9280-6350a839034d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5.0\n"
          ]
        }
      ],
      "source": [
        "def calculadora(n1, n2, operacao):\n",
        "  if(operacao == \"soma\"):\n",
        "    resultado = n1 + n2\n",
        "  elif (operacao == \"subtracao\"):\n",
        "    resultado = n1 - n2\n",
        "  elif (operacao == \"multiplicacao\"):\n",
        "    resultado = n1 * n2\n",
        "  elif (operacao == \"divisao\"):\n",
        "    resultado = n1 / n2\n",
        "  else:\n",
        "    print(\"operação invalida\")\n",
        "  return resultado\n",
        "print (calculadora(10,2,\"divisao\"))\n"
      ]
    }
  ]
}