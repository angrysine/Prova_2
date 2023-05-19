# Prova de programção

## 1. Introdução

Este projeto faz a tartaruga andar e voltar em uma rota
```
ros2 run turtlesim turtlesim_node
```

O código do robô pode ser executado com o comando:

```
python3 programa.py
```

## 2. Estrutura de dados

usamos uma pilha para armazenar os dados de ida e após usarmos cada ponto botamos eles na pilha que será usada na volta
## 3. Código

O código do robô foi feito em python3 e utiliza a biblioteca rclpy do ros2 para criar um nodo que controla o robô. O código do robô cria uma fila e insere nela os pontos de navegação que o robô deve percorrer. O robô percorre os pontos de navegação que estão na pilha e quando chega no último ponto, ele volta para o primeiro ponto usando a pilha. 


