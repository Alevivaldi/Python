{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPnDhXudgxjRgDV0RSZA7om"
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
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sO1cgpXhedVU",
        "outputId": "2e86e30e-885a-4719-fc0a-ba9755064b20"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "regue as batatas\n",
            "regue as batatas\n",
            "regue as batatas\n",
            "regue os tomates\n",
            "regue os tomates\n",
            "regue os tomates\n"
          ]
        }
      ],
      "source": [
        "\n",
        "def regar(k):\n",
        "  while (k < 6):\n",
        "    if (k < 3):\n",
        "      print(\"regue as batatas\")\n",
        "    else:\n",
        "      print(\"regue os tomates\")\n",
        "    k+=1\n",
        "k=0\n",
        "regar(k)"
      ]
    }
  ]
}